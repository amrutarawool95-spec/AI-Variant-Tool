# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install necessary C-compilers for cyvcf2, then python packages
RUN apt-get update && apt-get install -y gcc zlib1g-dev libbz2-dev libcurl4-openssl-dev liblzma-dev \
    && pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
