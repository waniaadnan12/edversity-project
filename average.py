def average(numbers):
    """Return the average of a list of numbers.

    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot compute average of an empty list")
    return sum(numbers) / len(numbers)
