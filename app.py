from flask import Flask, request
from flask_limiter import Limiter
import yaml
import os

# Create a new Flask app
app = Flask(__name__)

# Initialize rate limiting for the app with a limit of 5 requests per minute by default
limiter = Limiter(app, default_limits=["5 per minute"])

# Create an empty list to store IP addresses
ip_addresses = []

# Define a route for the app that returns the user's IP address
@app.route('/', methods=['GET'])
@limiter.limit("2 per minute") # Set a rate limit of 2 requests per minute for this route
def get_ip():
    # Get the user's IP address from the request object
    ip = request.remote_addr
    # Add the user's IP address to the list of IP addresses
    ip_addresses.append(ip)

    # Check the 'Accept' header to determine the response format
    accept_header = request.headers.get('Accept', 'text/plain')
    if 'text/html' in accept_header:
        # Return an HTML response
        return f"<h1>Your IP address is {ip}</h1>"
    elif 'application/xml' in accept_header:
        # Return an XML response
        return f"<ip><address>{ip}</address></ip>",  {'Content-Type': 'application/xml'}
    elif 'application/yaml' in accept_header:
        # Return a YAML response
        return yaml.dump({'ip': {'address': ip}}), {'Content-Type': 'application/yaml'}
    else:
        # Return a plain text response
        return f"Your IP address is {ip}", {'Content-Type': 'text/plain'}

# Define a route for the app that returns the list of IP addresses
@app.route('/ips', methods=['GET'])
def get_ip_addresses():
    # Return the list of IP addresses in JSON format
    return {'ip_addresses': ip_addresses}, {'Content-Type': 'application/json'}

# Define an error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    # Return a plain text response with a 404 status code
    return '404 Error: Page not found', 404

# Define an error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    # Return a plain text response with a 500 status code
    return '500 Error: Internal server error', 500

# Start the Flask app
if __name__ == '__main__':
    # Get the port number from the environment variables or use a default value of 8080
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
