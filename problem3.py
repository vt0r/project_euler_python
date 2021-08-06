#!/usr/bin/env python
# --------------------
# Project Euler - Problem 3
#
# Title: Largest prime factor
#
# Description: The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Our number from above
number = 600851475143

# Divisor - starts at 2
divisor = 2

# Determine factors of our number that are prime
def lrg_prime(num, div) -> int:
    while div < num:
        evendiv = num % div == 0
        quo = num / div
        if evendiv and quo > 1:
            num = quo
            div = 2
        else:
            div = div + 1
    return int(num)

# Largest prime factor
lpf = lrg_prime(number, divisor)

# Print the largest result
print(f"Largest prime factor: {lpf}")
