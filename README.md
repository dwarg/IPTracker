## Project description
This is a simple Flask application that returns the IP address of the client making the request. It includes rate limiting using Flask-Limiter to limit the number of requests per minute. It also supports different content types in the response based on the Accept header in the request. The application can be run as a Docker container and deployed to Kubernetes or Openshift. The Dockerfile includes multi-stage build to optimize the size of the image. The application also handles 404 and 500 errors with custom error pages.

The project consists of three files:

* **app.py** - contains the source code for the Flask application, which allows users to retrieve their IP address in various formats (plain text, HTML, XML, YAML). The file also contains limits on the number of requests to prevent excessive use of the application.
* **Dockerfile** - a Docker configuration file that allows you to build a Docker image containing the Flask application and its dependencies.
* **deployment.yaml** - this file is a Kubernetes configuration file that defines a Deployment for a Flask application. The Deployment specifies how many replicas of the application should be created, how to deploy the application, and how to manage it.
* **service.yaml** - this file is a Kubernetes configuration file that defines a Service for the Flask application.

## Installation
* Clone the repository: `git clone https://github.com/dwarg/IPTracker.git`
* Build the Docker image: `docker build -t image_name/app:latest .`
* Push the Docker image to your Docker registry: `docker push image_name/app:latest`
* Run the container by executing the command `docker run -p 8080:8080 image_name:tag`, where image_name and tag are the name and version of the image, and 8080 is the port number on the host.
* Apply the Kubernetes deployment and service files: `kubectl apply -f deployment.yaml` and `kubectl apply -f service.yaml`

## Usage
Once the application is deployed, you can access it by visiting the NodePort of the service. You can get the NodePort by running `kubectl get services`.

The application has two endpoints:

* `'/'`: Returns the user's IP address in the requested format. Supported formats are 'text/html', 'application/xml', 'application/yaml', and 'text/plain'. By default, the endpoint returns a plain text response.
* `'/ips'`: Returns a JSON object containing a list of all IP addresses that have accessed the '/' endpoint.

## Deployment
The Kubernetes deployment and service files are included in the repository. The deployment file (**deployment.yaml**) specifies the desired number of replicas for the application, the Docker image to use, and resource limits.

The service file (**service.yaml**) exposes the deployment as a NodePort service, allowing external traffic to reach the application.

To deploy the application, run the following commands:

* Create a namespace for the application by executing the command `kubectl create namespace namespace_name`
* Run the command `kubectl apply -f deployment.yaml` to deploy the application on the cluster.
* Run the command `kubectl apply -f service.yaml` to create a Service for the application.
* To get the IP address of the Service, run the command `kubectl get service -n namespace_name`
* Go to the web browser and enter the Service IP address in the format `http://service_IP` or `https://service_IP` depending on the configuration.