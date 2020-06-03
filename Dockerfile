# which python lightweight iso using
FROM python:3.7-alpine   

#whic company or who ever maintain this mea the author
MAINTAINER BlackCode Technologies

# run pytho in unbufferes mode
ENV PYTHONUNBUFFERED 1

# Install dependency to create a requiremnets .txt
COPY ./requirements.txt /requirements.txt 

RUN apk add --update --no-cache postgres-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgres-dev
# now install dependency in iso
RUN pip install -r /requirements.txt

RUN apk .tmp-build-deps
# create a  director to store all the our system and all files into
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# cresate auser that gonna run useing docker with name "user" for security purpose if we dont use then docker run this by root access
RUN adduser -D user
USER user


