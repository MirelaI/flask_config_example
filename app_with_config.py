import os
from flask import Flask

app = Flask('MyDemoApp')

config_file = 'config.json'
# The check below is to see if you have the
# config file defined and if you do not, it will display
# basic guidelines steps to set the config file.
if not os.path.isfile(config_file):
    app.logger.error(
        "Your config.json file is missing." +
        "You need to create one in order for this demo app to run." +
        "Please check the README.md file in order to set it up."
    )
else:
    # We are in the case where we have the config file.
    #
    # The line below is the magic statement that is going
    # to load our configuration from the config.json file.
    # After the line below is executed the config defined
    # in config.json will be available in the app variable.
    # Example on how you can get the config values:
    # secret_key = app.secret_key
    # OR
    # secret_key = app.config['SECRET_KEY']
    app.config.from_json(config_file)

@app.route('/my_key')
def my_key():
    my_config_secret_key = app.config['SECRET_KEY']

    if my_config_secret_key:
        app.logger.debug("Your secret key is: " + my_config_secret_key)
    else:
        app.logger.debug("No SECRET_KEY defined in the config.json")

    return "You should see your secret key in the terminal output"


app.run(debug=True)