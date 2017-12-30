# Trabalho Prático de Métodos Numéricos - Parte 1
# Métodos da Bisseção e Newton para aproximação de raízes
# Professor(a): Lilian Ferreira Berti
# Universidade Federal de Mato Grosso do Sul
# Aluno: Daniel de Faria Godoi (danielfgodoi@gmail.com)

import sys
from sympy import *

# Method for checking the relative error given xk and xk+1
def relativeError(xk, xk_1):
	num = (xk_1 - xk)
	if num < 0:
		num = num * -1
	den = xk_1
	if den < 0:
		den = den * -1
	print("error=" + str((num/den)) + "\n")
	return num/den

# Method for executing the Newton Method given
# the function
# the error bound (aka epsilon)
# the approximated roots (aka initial approximation)
def run(f, e, ar):
	print("Running Newton Method => approximate roots")

	# Calculate the derivative
	df = f.diff()

	# Array to store the approximated roots
	approx_roots = []
	
	for x in range(len(ar)):
		print("\nApproximating root for r" + str(x+1) + "=" +  str(ar[x]))

		max_it = 1000
		k = 0
		xk = ar[x]
		f_xk = f.evalf(subs={'x':xk})
		df_xk = df.evalf(subs={'x':xk})
		xk_1 = xk - (f_xk / df_xk)
		
		print("k=" + str(k) + "\nx_" + str(k) + "=" + str(xk) + "\nx_" + str(k+1) + "=" + str(xk_1))

		while relativeError(xk, xk_1) >= e and k < max_it:
			k += 1
			xk = xk_1
			f_xk = f.evalf(subs={'x':xk})
			df_xk = df.evalf(subs={'x':xk})
			xk_1 = xk - (f_xk / df_xk)
			print("k=" + str(k) + "\nx_" + str(k) + "=" + str(xk) + "\nx_" + str(k+1) + "=" + str(xk_1))

		print("Criteria met!\nApproximated root is at", xk_1, "\n")
		approx_roots.append(xk_1)

	return approx_roots

# This function will be executed only if running Newton script alone
def main(argv):
	# Get f, l, u and error bounds from input
	f = input("Input f(x): ")
	e = input("Input error for Newton Method: ")
	x0 = []
	x0.append(float(input("Input initial approximation (x0): ")))

	# Check for a valid error value
	try:
		e = sympify(e).evalf()

	except:
		print("\nThe error value is not a valid number")
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
	print("e = " + str(e))
	print("x0 = " + str(x0))

	ar = run(f, e, x0)

	# End script and print the approximated roots
	print("\nScript executed successfully!\n")
	print("Approximated roots for Newton Method\n" + str(ar) + "\n")

if __name__ == "__main__":
	main(sys.argv)
