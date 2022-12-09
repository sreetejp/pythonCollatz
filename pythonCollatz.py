# Collatz conjecture implementation in Python

def collatz(n: int) -> int:
    """
    Apply the Collatz conjecture to a given positive integer n.
    """
    # If n is 1, return 1
    if n == 1:
        return 1

    # If n is even, return n / 2
    if n % 2 == 0:
        return n // 2

    # If n is odd, return 3n + 1
    return 3 * n + 1

# Continuously prompt the user for a positive integer until they enter 'q' to quit
while True:
    # Read a positive integer or 'q' from the command line
    n_str = input("Enter a positive integer (or 'q' to quit): ")

    # If the user entered 'q', exit the program
    if n_str == 'q':
        break

    # Convert the string to an integer and apply the Collatz conjecture until it reaches 1
    n = int(n_str)
    while n != 1:
        n = collatz(n)
        print(n)

    # Print a message when the sequence reaches 1
   
