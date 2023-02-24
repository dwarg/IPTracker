FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y gcc
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8080
CMD ["python", "app.py"]