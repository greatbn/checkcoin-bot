FROM python:2.7.12
MAINTAINER saphi070@gmail.com

ENV PYTHONUNBUFFERED 0
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt


COPY app.py /app/
ENTRYPOINT ["python", "app.py"]
