#!/usr/bin/env python
# --------------------
# Project Euler - Problem 2
#
# Title: Even Fibonacci numbers
#
# Description: Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

# Start with a sum of 0 for sanity
# Type: int
sum = 0

# Set a max value of 4 million
# Type: int
max_val = 4000000

# Initial fibonacci array
# Type: List of ints
fibonacci = [1, 2]

# Add last two items in a given list and return the sum
def sum_last_two(mylist: list) -> int:
    return mylist[-2] + mylist[-1]

# Append sum of two previous numbers until we hit our given max value
while sum_last_two(fibonacci) < max_val:
    fibonacci.append(sum_last_two(fibonacci))

# Sum of even sums
for num in range(0, len(fibonacci)):
    if fibonacci[num] % 2 == 0:
        sum = sum + fibonacci[num]

# Print output
print(f"Numbers: {fibonacci}\n\nSum of all even numbers: {sum}")