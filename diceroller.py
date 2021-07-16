import random
import sys

def dice(n):
    print(f"You rolled a {random.randint(1, n)}")

dice(int(sys.argv[1]))
