FROM python:latest
LABEL Maintainer="roushan.me17"
WORKDIR /venv/
COPY oranges.py /venv/
RUN chmod +x  /venv/*
CMD [ "python3", "./oranges.py"]
