FROM python:3.9
WORKDIR /usr/src/app
RUN python -m pip install \
        discord
WORKDIR /app
#COPY README.md .
