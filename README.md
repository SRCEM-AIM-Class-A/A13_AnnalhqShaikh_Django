# Django Multi-app

This repository contains a multi-app Django project. The project is containerized using Docker and can be easily deployed using Docker Hub.

## Table of Contents

- [Setup](#setup)
- [Running the Django Server Locally](#running-the-django-server-locally)
- [Building and Running the Docker Container](#building-and-running-the-docker-container)
- [Pushing to Docker Hub](#pushing-to-docker-hub)
- [Pulling from Docker Hub](#pulling-from-docker-hub)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Setup

To get started with this project, you need to have the following installed on your machine:

- Python 3.10 or higher
- Docker
- Git

## Running the Django Server Locally

To run the Django server locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/SRCEM-AIM-Class-A/A13_AnnalhqShaikh_Django.git
    cd A13_AnnalhqShaikh_Django
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/Scripts/activate  # On Windows
    source env/bin/activate      # On macOS/Linux
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirement.txt
    ```

4. Run the Django server:

    ```bash
    python manage.py runserver
    ```

## Building and Running the Docker Container

To build and run the Docker container, follow these steps:

1. Build the Docker image:

    ```bash
    docker build -t annalhq/django-multiapp .
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 annalhq/django-multiapp
    ```

3. Open your browser and navigate to `http://localhost:8000` to see the application running.

## Pushing to Docker Hub

To push the Docker image to Docker Hub, follow these steps:

1. Log in to Docker Hub:

    ```bash
    docker login -u <your-docker-username>
    ```

2. Tag the Docker image:

    ```bash
    docker tag annalhq/django-multiapp <your-docker-username>/django-multiapp
    ```

3. Push the Docker image to Docker Hub:

    ```bash
    docker push <your-docker-username>/django-multiapp
    ```

## Pulling from Docker Hub

To pull the Docker image from Docker Hub, follow these steps:

1. Pull the Docker image:

    ```bash
    docker pull annalhq/django-multiapp
    ```

2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 annalhq/django-multiapp
    ```

3. Open your browser and navigate to `http://localhost:8000` to see the application running.

## Project Structure

The project structure is as follows:

```
env/
    ...
project/
    db.sqlite3
    Dockerfile
    Jenkinsfile
    manage.py
    README.md
    requirement.txt
    app1/
        ...
    app2/
        ...
    app3/
        ...
    project/
        ...
    static/
        ...
    templates/
        ...
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.