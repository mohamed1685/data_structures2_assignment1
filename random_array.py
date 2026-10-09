import random


def generate_random_ints(length: int) -> list[int]:
    return [random.randint(0, 10000) for _ in range(length)]