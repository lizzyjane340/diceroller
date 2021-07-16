import random
import sys

def dice(n):
    print(f"You rolled a {random.randint(1, n)}")

if len(sys.argv) != 2:
    print("Only takes one argument!")
    sys.exit(1)

dice(int(sys.argv[1]))


