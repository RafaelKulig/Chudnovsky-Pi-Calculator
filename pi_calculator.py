from decimal import Decimal, getcontext, ROUND_FLOOR
import argparse
import sys

def setup():
    """
    Initial setup for decimal precision and recursion limit.
    """
    getcontext().rounding = ROUND_FLOOR     # This line will round the numbers down to  the closest integer
    sys.setrecursionlimit(100000)           # Set the maximun amount for a recursive function

def factorial(n:int):
    """
    Recursiv function that return the factorial of a number 

    Inputs: n -> Number that will be factoraded 
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def get_iterated_value(k: int) -> Decimal:
    """
	Return the Iterations as given in the Chudnovsky Algorithm.
	k iterations gives k-1 decimal places.
    Since we need k decimal places make iterations equal to k+1
	
	Inputs:	k -> Number of Decimal Digits to get
	"""
    k += 1
    getcontext().prec = k
    total = Decimal(0)
    for i in range(k):
        dividend = factorial(6 * i) * (13591409 + 545140134 * i)
        divisor = factorial(3 * i) * (factorial(i) ** 3) * ((-262537412640768000) ** i)
        total += Decimal(dividend) / Decimal(divisor)       # https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    return total


def get_value_of_pi(k: int) -> Decimal:
    """
	Returns the calculated value of Pi using the iterated value of the loop
	and some division as given in the Chudnovsky Algorithm
	Input: k -> Number of Decimal Digits upto which the value of Pi should be calculated
	"""
    iterator = get_iterated_value(k)
    up = Decimal(426880) * Decimal(10005).sqrt()        # https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    pi = up / iterator
    return pi

def main():
    setup()
    
    parser = argparse.ArgumentParser(description="Show number pi up to the nth decimal place.")
    parser.add_argument('-n', type=int, help='Number of decimal places to be shown.')
    args = parser.parse_args()

    if args.n is not None:
        entry = args.n
    else:
        while True:
            print("Enter the number of digits up to which π should be calculated or type 'quit' to exit:")
            entry = input(">>> ").strip()
            if entry.lower() == "quit":
                return
            if not entry.isdigit():
                print("Please enter a valid positive integer.")
                continue
            entry = int(entry)
            break

    if entry < 1:
        print("Please enter a positive integer greater than 0.")
        sys.exit(1)

    print(get_value_of_pi(entry))

if __name__ == "__main__":
    main()