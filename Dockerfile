# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py .

# Specify the command to run the application
CMD ["python", "app.py"]
