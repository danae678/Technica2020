FROM python:3.8-slim-buster 

COPY bots/retweetbot.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "retweetbot.py"]