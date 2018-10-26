FROM python:3.5.6-alpine3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "./app.py"]
CMD ["app.py"]