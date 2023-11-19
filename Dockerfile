
FROM python:3.9

ENV HOMIE_TOKEN=#<your_token_here>

RUN python3 -m pip install -U discord.py

COPY homie.py /app/homie.py

WORKDIR /app

CMD ["python", "homie.py"]
