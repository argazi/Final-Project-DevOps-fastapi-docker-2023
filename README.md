# Final-Project-DevOps-fastapi-docker-2023
Final-Project-DevOps-fastapi-docker-2023

How to Run:

docker build -t my-python-app .

docker run -d -e SPRING_ADDR="10.100.102.41:8080" -p 8000:8000 --name my-python-app-container my-python-app
