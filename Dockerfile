FROM public.ecr.aws/bitnami/python:3.8

WORKDIR /home

COPY . .
ENV PYTHONPATH "${PYTHONPATH}:${WORKDIR}"
CMD ["python", "main.py"]
