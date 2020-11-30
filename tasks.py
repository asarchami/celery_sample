from time import sleep
from datetime import datetime
from celery import Celery

BROKER_URL = "redis://localhost:6379/0"
app = Celery("tasks", broker=BROKER_URL)


@app.task
def add(x, y):
    sleep(2)
    res = x + y
    with open(
        f'logs/{datetime.strftime(datetime.now(), "%m-%d-%Y_%H:%M:%S")}', "w"
    ) as _file:
        _file.write(str(res))
    return res
