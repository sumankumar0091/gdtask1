FROM python:3.6.1-alpine
WORKDIR /gdtask1
ADD . /gdtask1
RUN pip install -r requirements.txt
CMD python3 app.py 
