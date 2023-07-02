# Posts Parser with Telegram/Discord Output
This fun little script parses posts from my website and tells you if there are any new ones.

# Screenshots
<details>

<summary>Collapse me</summary>

![image](https://github.com/womblee/telegram-discord-posts-parser/assets/52250786/a5b76bae-ab8b-4192-8658-bef955a278ee)

![image](https://github.com/womblee/telegram-discord-posts-parser/assets/52250786/a716a857-6088-4100-be92-c87e76279f73)

* There are also discord screenshots, but I am lazy to add them...

</details>

# How does it work?
When used for the first time, it creates a text file called parsed.txt.
This text file contains hrefs to articles on my website.

Over time when new posts are released, parsed.txt will eventually get outdated.
What happens next? This program checks for the mismatches between the new and old data.
If it finds any, it outputs them in your Telegram/Discord channel.

# What is required?
* 🦫 **IF YOU'RE PLANNING TO USE TELEGRAM:**
  
     `BOT Token`, you can get it by creating a bot in BotFather.

     `Channel ID`, where the messages will be posted.

* 🐻 **IF YOU'RE PLANNING TO USE DISCORD:**
  
     `YOUR token`, since it works like a self-bot.

     `Channel ID`, provide your wanted channel by enabling developer features and pressing 'Copy Channel ID' on any channel you want.


* 🐋 **YOU CAN USE BOTH AT THE SAME TIME!**

  # Installation
  Run `pip install -r requirements.txt`
  Run `python notify.py`

  Ideally you should run `notify.py` every 5-30 minutes or so...
