import random
import sys

def dice(n):
    print(f"You rolled a {random.randint(1, n)}")

if len(sys.argv) != 2:
    print("Only takes one argument!")
    sys.exit(1)

try:
    sides = int(sys.argv[1])
except ValueError:
    print("Argument must be a number!")
    sys.exit(1)

dice(sides)


