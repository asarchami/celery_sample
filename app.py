import time
from tasks import add

if __name__ == "__main__":
    t1 = time.perf_counter()
    for num in range(10):
        add.delay(num, num)
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")