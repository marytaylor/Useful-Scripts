# Found great example of a list comprehension that I want to have in mind for the future.

vals = [expression for valu in collection if condition]

# the above is equivalent to the following

vals = []
for value in collection:
		if condition:
			vals.append(expression)

# Example in use:
even_squares = [ x * x for x in range(10) if not x % 2]
# return result
even_squares

# [0, 4, 16, 36, 64]