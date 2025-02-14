# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]
