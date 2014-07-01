def test_pass():
	assert 1 == 1

import my_functions as F
def test_factorial_simple():
	assert F.factorial(3) == 6