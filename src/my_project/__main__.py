from typing import List


def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        int: The sum of the two input integers.
    """
    return a + b


def multiply_numbers(numbers: List[int]) -> int:
    """Multiply a list of integers and return the result.

    Args:
        numbers (List[int]): A list of integers to multiply.

    Returns:
        int: The product of all integers in the input list.
    """
    result = 1
    for number in numbers:
        result *= number
    return result


def greet(name: str) -> str:
    """Generate a greeting message for the given name.

    Args:
        name (str): The name to include in the greeting message.

    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"


def main() -> None:
    """Main function to execute some random functions."""
    sum_result = add_numbers(3, 7)
    print(f"Sum: {sum_result}")

    product_result = multiply_numbers([2, 3, 4])
    print(f"Product: {product_result}")

    greeting = greet("Alice")
    print(greeting)


if __name__ == "__main__":
    main()
