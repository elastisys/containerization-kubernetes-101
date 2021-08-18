# We use the most stable Python 3 out there
FROM python:3

# All files will wind up in the /app directory in the container
WORKDIR /app

# Containers should always avoid running as root, so we create a
# less privileged user
RUN useradd -ms /bin/bash runner

# Now make the user be "runner"
USER runner

# Copy the file listing the dependencies
COPY src/requirements.txt /app

# Install all requirements as specified by the requirements.txt file
# on the container image
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code to /app now that we have the dependencies
COPY src/ /app

# Add metadata that this container will want to open port 5000
EXPOSE 5000

# The command that will run when container starts
ENTRYPOINT ["python3"]

# The default argument(s), passed to the entrypoint
CMD ["app.py"]
