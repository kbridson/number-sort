import random


def sort_numbers(numbers):
    print(numbers)
    numbers.sort()
    print(numbers)


numbers = random.sample(range(1, 100), 5)
sort_numbers(numbers)
