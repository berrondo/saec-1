FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
RUN mkdir /app/staticfiles
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
COPY ./contrib/docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh
