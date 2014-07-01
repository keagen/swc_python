def square(x):
	"Here's our fist docstring"
	return x * x


def factorial(x):
	"Calculates the factorial of x"
	fac = 1
	for n in range (1, x + 1):
		fac = fac * n
	print fac 