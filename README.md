# Gluon SMLight - Antenna Reset

**Version:** 0.1.0  
**Domain:** `gluon_smlight`  
This custom component for Home Assistant provides the ability to reset antennas by making HTTP requests to specific endpoints.

## Features
- Adds two services to Home Assistant for resetting antennas: `antenna_1a_Zigbee` and `antenna_1a_ESP32`.
- Uses basic HTTP authentication to securely access the antenna reset endpoints.

## Installation

### Step 1: Modify IP addresses, user, and password
In the `__init__.py` file, update the IP addresses, user, and password fields according to your system's configuration:
```python
url = "http://<your_ip_address>/api2?action=4&cmd=1"  # Update the URL
user = "your_user"  # Replace with your username
password = "your_password"  # Replace with your password
```
And:
```python
url = "http://<your_ip_address>/api2?action=4&cmd=3"  # Update the URL
user = "your_user"  # Replace with your username
password = "your_password"  # Replace with your password
```
### Step 2: Create the custom component directory
Create a new directory called gluon_smlight inside the custom_components folder in your Home Assistant installation.
Place the following files inside the `gluon_smlight` directory:
`__init__.py`
`manifest.json`

### Step 3: Add the component to Home Assistant
In your `configuration.yaml` file, add the following line:
```yaml
# Antenna reset service
gluon_smlight:
```

### Step 4: Restart Home Assistant
Restart your Home Assistant instance for the changes to take effect.

### Usage
Once the component is set up, you will have access to two new services in Home Assistant:

- `gluon_smlight.antenna_1a_Zigbee`
  
This service sends a reset request to the Zigbee antenna.

- `gluon_smlight.antenna_1a_ESP32`
  
This service sends a reset request to the ESP32 antenna.


You can call these services from Home Assistant's interface or integrate them into your automations.
