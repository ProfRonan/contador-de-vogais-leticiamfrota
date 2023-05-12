"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    """
    Takes in a string and returns the number of vowels in the string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    i = 0
    string = string.lower()
    n = len(string)
    for c in string:
        if c in 'aeiou':
            i += 1
    return i