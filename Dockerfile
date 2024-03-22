FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install requests beautifulsoup4

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]