# TODO: add reverse sort option
import random


def sort_numbers(numbers):
    print(numbers)
    numbers.sort()
    print(numbers)


numbers = random.sample(range(1, 100), 10)
sort_numbers(numbers)
