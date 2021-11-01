FROM oraclelinux:8-slim

COPY ./app /app

RUN ls -la &&\ 
microdnf install python39 &&\
microdnf install python39-pip &&\
microdnf clean all &&\
pip3.9 install -r /app/requirements.txt  

EXPOSE 5000

CMD python3.9 /app/mainApp.py
