# FROM eclipse-mosquitto:latest
FROM python:3.9-slim

# RUN pip install pandas json paho-mqtt
RUN apt-get update && apt-get install -y \
    mosquitto \
    mosquitto-clients \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pandas paho-mqtt

WORKDIR /app

COPY data /data

COPY py_files /py_files

# RUN python py_files/geojson.py


ENTRYPOINT [ "bash" ]
CMD [ "bash" ]