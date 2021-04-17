FROM python:3.8

ADD requirements.txt /requirements.txt

ADD main.py /main.py

ADD okteto-stack.yaml /okteto-stack.yaml

RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./app /app

CMD ["python3", "main.py"]
