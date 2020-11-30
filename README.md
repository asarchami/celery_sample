# Celery

* Install redis: `docker run --name redis-db -d -v redis-data:/data -p 6379:6379 redis:6-alpine`
* install celery with redis: `pip install celery[redis]`
* create a task like `tasks.py`
* execute celery `celery -A tasks worker -l info` or `celery -A tasks worker -l info -c 3` for limiting concurrency
* call a task from another app line `app.py`