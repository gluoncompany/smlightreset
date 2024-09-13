DOMAIN = "gluon_smlight"

from homeassistant.components.button import ButtonDeviceClass, ButtonEntity
import requests

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def antenna_1a_zigbee(call):
        """Handle the service call."""
        
        # URL of the endpoint you want to make the GET request to
        # API1 Old
        #url = "http://192.168.1.2/api?action=8&cmd=1"
        # API2 New
        url = "http://192.168.1.2/api2?action=4&cmd=1"

        # Authentication data
        user = "user"
        password = "password"

        # Build the basic authentication header
        authentication = requests.auth.HTTPBasicAuth(user, password)

        # Make the GET request with basic authentication
        response = requests.get(url, auth=authentication)

        # Check the response status code
        if response.status_code == 200:
            # The request was successful
            print(response.text)
        else:
            # The request failed
            print("Error:", response.status_code)

    def antenna_1a_esp32(call):
        """Handle the service call."""

        # URL of the endpoint you want to make the GET request to
        # API1 Old
        #url = "http://192.168.1.2/api?action=8&cmd=3"
        # API2 New
        url = "http://192.168.1.2/api2?action=4&cmd=3"

        # Authentication data
        user = "user"
        password = "password"

        # Build the basic authentication header
        authentication = requests.auth.HTTPBasicAuth(user, password)

        # Make the GET request with basic authentication
        response = requests.get(url, auth=authentication)

        # Check the response status code
        if response.status_code == 200:
            # The request was successful
            print(response.text)
        else:
            # The request failed
            print("Error:", response.status_code)


    hass.services.register(DOMAIN, "Antenna_1a_Zigbee", antenna_1a_zigbee)
    hass.services.register(DOMAIN, "ASntenna_1a_ESP32", antenna_1a_esp32)

    # Return boolean to indicate that initialization was successful.
    return True