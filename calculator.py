"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    if isinstance(first_term, int) and isinstance(second_term, int):
        return first_term // second_term
    else:
        return first_term / second_term
