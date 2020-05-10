from contextlib import contextmanager
from time import time


@contextmanager
def timing(description: str) -> None:
    start = time()
    yield
    ellapsed_time = time() - start

    print(f"{description}: {ellapsed_time}")


with timing("List Comprehension Example"):
    s = [x for x in range(10_000_000)]
