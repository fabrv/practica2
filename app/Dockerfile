# Define a python image that uses requirements.txt to install dependencies
FROM python:3.6
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]
