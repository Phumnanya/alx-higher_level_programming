<<<<<<< HEAD
jk
=======
#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.
    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
>>>>>>> f1b5ed84f130e37ed00e3493287306c02fa0a7f3
