# Employee Profile Application

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd employee-profile-app
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application locally:
    ```bash
    flask run
    ```

5. Run the application with Gunicorn:
    ```bash
    gunicorn --workers 3 --bind unix:/home/ubuntu/employee-profile-app.sock wsgi:app
    ```

6. To configure Nginx, copy the contents of `nginx.conf` to `/etc/nginx/sites-available/default` and restart Nginx:
    ```bash
    sudo cp nginx.conf /etc/nginx/sites-available/default
    sudo systemctl restart nginx
    ```

## Deployment

Follow the instructions to deploy on an EC2 instance with the provided user data script.
