# Logan v0.0.1
This is a project for a voice assistant named Logan to implement it in your projects
## How to build
* First you need to change the person parameters in the main script.
* Then you need to specify the API token openai in the gpt.py script
* Also, if you want, you can specify a start message from the system to change the assistant's name or give him instructions.
* Install all required dependencies with the `pip install requirements.txt`.
* To add commands to the bot, you need to add your function anywhere before the execute_command_with_name() function, and then specify your command in the commands in the format ("start-word 1", "start-word 2"): function_name.
##
* The bot will execute given commands or simply communicate with the user
* You can choose multiple voice options by changing play_voice_assistant_speech() and setup_assistant_voice()
