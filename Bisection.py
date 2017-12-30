# Trabalho Prático de Métodos Numéricos - Parte 1
# Métodos da Bisseção e Newton para aproximação de raízes
# Professor(a): Lilian Ferreira Berti
# Universidade Federal de Mato Grosso do Sul
# Aluno: Daniel de Faria Godoi (danielfgodoi@gmail.com)

import sys
from sympy import *

# Method for finding roots given
# the function
# the initial interval
# the number of required roots
def findRoots(f, l, u, n=1):

	print("\nRunning Bisection Method => find roots")

	try:
		# Test if is a valid result
		f_l = f.evalf(subs={'x':l})
		f_u = f.evalf(subs={'x':u})
		float(f_l)
		float(f_u)

		if (f_l * f_u) < 0:
			criterion = True

		else:
			criterion = False

	except:
		print("\nThe function is not a valid function (please check the syntax)\nTip: the function must be specified in terms of x")
		exit()

	if not criterion:
		print("\nThe criteria f(a)*f(b) < 0 were not met, ending script")
		exit()
	
	else:
		print("\nThe criteria f(a)*f(b) < 0 were met, proceed")

		if n == 1:
			return [l, u]

		else:
			# Search for n roots
			print("Trying to find " + str(n) + " roots as specified")
			x = int(l)
			y = int(u)
			array = []
			roots = []

			for x in range(int(l), int(u)+1):
				array.append([x, f.evalf(subs={'x':x})])

			x = 0
			for y in range(x+1, len(array)):
				if (array[x][1] * array[y][1]) < 0:
					roots.append([array[x][0], array[y][0]])
				x += 1
			
			if str(len(roots)) == str(n):
				print("Found the " + str(n) + " roots")

			else:
				print("Didn't find the " + str(n) + " roots, but found " + str(len(roots)) + " roots")

			for x in range(len(roots)):
				print("r" + str(x+1) + " is in " + str(roots[x]))

			return roots

# Method for executing the Bisection Method given
# the function
# the error bound (aka epsilon)
# the inital roots' interval
def run(f, e, r):
	# Array to store the approximated roots
	approx_roots = []

	print("\nRunning Bisection Method => approximate roots\n")

	for x in range(len(r)):
		print("Approximating root for r" + str(x+1), str(r[x]))

		max_it = 1000
		i = 0
		a = r[x][0]
		b = r[x][1]
		error = (b - a)

		while error >= e and i < max_it:

			c = float((a + b) / 2)
			i += 1

			# Test wich side to take
			f_a = f.evalf(subs={'x':a})
			f_b = f.evalf(subs={'x':b})
			f_c = f.evalf(subs={'x':c})

			print("i=" + str(i) + " a=" + str(a) + " b=" + str(b) + " c=" + str(c), end=' ')

			if f_c == 0:
				print("f(c) = 0 ending program")
				exit()

			elif (f_a * f_c) < 0:
				b = c

			elif (f_c * f_b) < 0:
				a = c

			else:
				print("\nNone of the subintervals are negative, i.e., f(a)*f(c) > 0 and f(c)*f(b) > 0. Ending program with last results")
				exit()

			error = (b - a)
			print("error=" + str(error))

		print("\nCriteria met!\nApproximated root is at " + str(c) + "\n\n")
		approx_roots.append(c)

	return approx_roots

# This function will be executed only if running Bisection script alone
def main(argv):
	# Get f, l, u and error bounds from input
	f = input("Input f(x): ")
	i = input("Input interval (l, u): ")
	e = input("Input error for Bisection Method: ")
	n = input("Input number of roots to find: ")

	# Check for a valid error value
	try:
		e = sympify(e).evalf()

	except:
		print("\nThe error value is not a valid number")
		exit()

	# Parse interval to get lower and upper values
	i = i.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",", " ")
	
	if len(i.split()) == 2:
		l = float(i.split()[0])
		u = float(i.split()[1])
		if l > u:
			print("\nThe interval is malformatted (lower value is greater than upper)\nInput interval in the pattern 'l, u' or (l, u) or [l, u]")
			exit()
	else:
		print("\nThe interval is malformatted (missing values)\nInput interval in the pattern l, u or (l, u) or [l, u]")
		exit()

	# Replace X by x if mistyped
	f = f.replace("X", "x")
	# Relace e* by E* if mistyped
	f = f.replace("e*", "E*")
	# Relace e^ by E^ if mistyped
	f = f.replace("e^", "E^")
	# Convert string to sympy expression
	f = sympify(f)

	print("\nf(x) =", f)
	print("l = " + str(l) + " u = " + str(u))
	print("e = " + str(e))

	r = findRoots(f, l, u, n)
	ar = run(f, e, r)

	# End script and print the approximated roots
	print("Script executed successfully!\n")
	print("Approximated roots for Bisection Method\n" + str(ar) + "\n")

if __name__ == "__main__":
	main(sys.argv)
