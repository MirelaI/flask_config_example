# Setup Flask configuration

When you build your Flask app, you might need a place where to store common configuration values. A good example of values that you should store in a configuration file is be secret keys of different APIs that you want to use in your project, like [MailGun App](https://www.mailgun.com/) or [WeatherApp](http://openweathermap.org/api) or any other API.

In the same time you do not want to expose this key in the github repository that you use for your Flask app/project. The instructions below is how to have this setup without exposing your keys to the world.

## Instructions

### Github repo

You need a Github repository, like this one for example. Or your work repository for the project.

### Local copy
Make sure you have a local copy of the git repository. If not, please clone it:

```bash
git clone <your_repo_url>
cd your_repo_folder
```

Now you should be in your terminal in your repository folder.

### Create a config.json file
The config.json file, will sit in the root folder of your project.

```bash
touch config.json
open config.json
```

### Edit config.json

Using your preffered editor(Sublime, Atom, or any other) edit the config.json file by adding the keys that you need in your application. The content of your config.json file should look something similary with the example below:

```json
{
    "MAILGUN_SECRET_KEY": "your_mailgun_secretkey",
    "OTHER_APP_SECRET_KEY": "your_other_app_secret_key",
    "MY_APP_NAME": "AwesomeApp",
    "ENVIRONMENT": "production",
    ...
}

```
In the example above, `...` part means there can be other config values there and it's not necessary to be only API keys.

You can see an example of a config file in `config_example.json` present in this repostiory.

### Use config.json with Flask

In order to make use of the config values in your application, please have a read through the example provided in the app_with_config.py file, available in this repository. In short, you need to load your config into your application and the code statemend that will enable you to do this, it is:

```python
app = Flask("MyAwsomeApp")

app.config.from_json('config.json')
```

Now `app` will be holding the config values and we can access them by interogating the `app.config` dictionary. For example if I want to know the value of "MAILGUN_SECRET_KEY" I can now access it via:

```python
app.config["MAILGUN_SECRET_KEY"]
```

### Tell git to ignore your config

The last thing we want to do is to not push this config.json file to Github. We are going to use the power of .gitignore to do this.
Create a new file named .gitignore in your project folder.

```bash
touch .gitignore
open .gitignore
```

Since you also opened the .gitignore file, edit it by adding `config.json` string and save it. Your `.gitignore` file, should look exactly as the one defined in this repository.

By adding `config.json` into .gitignore file, we are telling git to ignore our configuration as we do not want to make it public.

We need to check now that git does not see `config.json` file, and we do this by usin the git status command.

```git
git status
```
You should see something similar to:
```
On branch master

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    .gitignore
    app_with_config.py

nothing added to commit but untracked files present (use "git add" to track)

```
You should not see `config.json` in the output above. If you see it, something went wrong when you setup the .gitignore file. Please have a read through [Git Ignore documentation](https://help.github.com/articles/ignoring-files/) to unblock you.

### You are almost done ...
Commit your changes and also add a README.md file, similary to this one, where you provide instructions to your colleagues, as they need to clone the repo and create a config.json file in order for the application to run properly.

```bash
touch README.md
# Add instructions to README.md
git add .
git commit -am "Setup for my application to work with config files"
git push origin master
```

Note: it can be the same secret key for your apps, if you work in a group. But please make sure the person who knows the keys shares them with the group via other methods than Github. Point in your README, that in order to get the secret key please contact 'Name of the colleague who is responsible of the keys'.

Please let me know if you have any questions!

