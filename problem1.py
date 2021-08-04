#!/usr/bin/env python

# The maximum value in the range of possible multiples
# Type: int
max_val = 1000

# The factor(s)
# Type: List of ints
factors = [3, 5]

# The list of even multiples
# Type: List of ints
multiples = []

# Sum starts at 0 so you know what's coming
# Type: int
sum = 0

# Determine whether a given value is a multiple of given factor(s)
def is_multiple(number: int, factors: list) -> bool:
  for factor in factors:
    if number % factor == 0:
      return True
      break
  return False

# Check to see if numbers in a given range are even multiples of given factors
for number in range(1, max_val):
  if is_multiple(number, factors):
    multiples.append(number)

# Sum all array elements
for m in range(0, len(multiples)):
  sum = sum + multiples[m]

# Print all elements and then the sum
print(f"Multiples: {multiples}\n\nSum: {sum}")
