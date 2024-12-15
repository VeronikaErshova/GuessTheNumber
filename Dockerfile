FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    python3-pyqt5 \
    python3-pyqt5.qtsvg \
    python3-pyqt5.qtwebengine \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .
COPY number.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "number.py"]