# Trabalho Prático de Métodos Numéricos - Parte 1
# Métodos da Bisseção e Newton para aproximação de raízes
# Professor(a): Lilian Ferreira Berti
# Universidade Federal de Mato Grosso do Sul
# Aluno: Daniel de Faria Godoi (danielfgodoi@gmail.com)

import sys
from sympy import *

import Bisection
import Newton

# Method for parsing values based on argv
def parser(argv):
	# Check if user wants to use the default function or input a new one
	print("Please, choose one of the options below")
	print("1. Input a new function with the interval and error bounds")
	print("2. Use the default function e^x-4*x^2 and interval (-1, 5)")
	opt = input("Option: ")

	f = None
	i = None
	e = None

	if opt == str(1):
		# Get f, l, u and error bounds from input
		f = input("Input f(x): ")
		i = input("Input interval (l, u): ")
		e_b = input("Input error for Bisection Method: ")
		e_n = input("Input error for Newton Method: ")

		# Check for a valid error value
		try:
			e_b = sympify(e_b).evalf()
			e_n = sympify(e_n).evalf()

		except:
			print("\nThe error value is not a valid number")
			exit()

	elif opt == str(2):
		f = "e**x-4*x**2"
		i = "-1 5"
		e_b = "10**-2"
		e_b = sympify(e_b).evalf()
		e_n = "10**-6"
		e_n = sympify(e_n).evalf()

	else:
		print("\nThis option is not available! Please, try again...")
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
	print("e_b = " + str(e_b))
	print("e_n = " + str(e_n))

	return f, l, u, e_b, e_n

def main(argv):
	# Parse needed variables
	f, l, u, e_b, e_n = parser(sys.argv)

	# Define the number of roots to find in the interval [l, u]
	n = 3
	
	# Run Bisection Method => findRoots
	# r is the roots intervals, i.e., for each root, it will have a tuple like [a, b]
	r = Bisection.findRoots(f, l, u, n)
	
	# Run Bisection Method => approximate roots
	ar_b = Bisection.run(f, e_b, r)
	
	# Run Newton Method using the approximated roots from Bisection
	ar_n = Newton.run(f, e_n, ar_b)
	
	# End script and print the approximated roots from both methods
	print("\nScript executed successfully!\n")
	print("Approximated roots for Bisection Method\n" + str(ar_b) + "\n")
	print("Approximated roots for Newton Method\n" + str(ar_n) + "\n")


if __name__ == "__main__":
	main(sys.argv)
