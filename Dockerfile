# syntax=docker/dockerfile:1

# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Copy the current directory contents into the container
COPY . .
# Install dependencies
RUN pip3 install -r requirements.txt


# Expose the port Streamlit will run on
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
