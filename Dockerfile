FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

ENV PYTHONUNBUFFERED 1
ENTRYPOINT [ "python", "./app.py" ]
