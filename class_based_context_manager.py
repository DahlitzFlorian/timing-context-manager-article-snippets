# class_based_context_manager.py

from time import time


class Timer(object):
    def __init__(self, description):
        self.description = description

    def __enter__(self):
        self.start = time()

    def __exit__(self, type, value, traceback):
        self.end = time()
        print(f"{self.description}: {self.end - self.start}")


with Timer("List Comprehension Example"):
    s = [x for x in range(10_000_000)]
