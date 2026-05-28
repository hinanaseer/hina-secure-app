FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app/ .

RUN useradd -u 1001 devopsuser && chown -R devopsuser:devopsuser /app
USER devopsuser

EXPOSE 5000

CMD ["python", "app.py"]