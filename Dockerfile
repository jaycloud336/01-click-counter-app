# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY counter_app.py /app/
COPY requirements.txt /app/
COPY templates/ /app/templates/
COPY static/ /app/static/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app's port
EXPOSE 5000

# Run the Flask app
CMD ["python", "counter_app.py"]
