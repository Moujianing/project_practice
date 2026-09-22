"""Print the first five Fibonacci numbers."""


def fibonacci(n):
    """Return the first n Fibonacci numbers as a list."""
    numbers = []
    a, b = 0, 1
    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b
    return numbers


if __name__ == "__main__":
    print(fibonacci(5))
