import os.path
import string
import requests
from lxml import html

# Tokens
TG_TOKEN = "1925596051:AAFdH2Xhd7zuPhV3r6BCmKmgRq3VGCRWcnt" # Telegram, you can get it by creating a bot in BotFather
DC_TOKEN = "NRczMDAxOFCzMjc5OTAzOTr0.Gmprgv.F2QJYPcrXL553zMGKreKtJQ2hwQRCc51oHyP1Y" # Discord, must be YOUR token and must NOT BE A BOT.

# Channels
TG_ID = "865351493" # Telegram, this should be your DM or some channel where the bot is present
DC_ID = "806245820217383857" # Discord, provide your wanted channel by enabling developer features and pressing 'Copy Channel ID' on any channel you want

# Debug, enable this if you are a developer
DEBUG = False

# Send message
def send_message(tar):
    if TG_TOKEN and TG_ID:
        requests.get(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage?chat_id={TG_ID}&text={tar}")

    if DC_TOKEN and DC_ID:
        OBJ = {
          "content": tar,
          "tts": False,
          "embeds": [],
          "components": [],
          "sticker_ids": [],
          "files": []
        }
        
        # You may try adding this to headers, since Discord is very strict in terms of Bots sending HTTP requests.
        # "User-Agent": "DiscordBot (https://discord.js.org, Node.js/v18.16.1)"
        # But it didn't work for me...
        requests.post(f"https://discord.com/api/v9/channels/{DC_ID}/messages", headers={"Authorization": DC_TOKEN}, json=OBJ)
        


# Parse page
SITE = requests.get("https://nlog.us/index.html")
PARSED = html.fromstring(SITE.content)

# Posts
POSTS = PARSED.xpath("//dl/dt/a")

PLACEHOLDER = []

for PS in POSTS:
    PLACEHOLDER.append("https://nlog.us/" + PS.get("href"))    

POSTS = PLACEHOLDER 
del(PLACEHOLDER) # Delete from memory

# Update
def update_file():
    with open("parsed.txt", "w") as FILE:
        for POST in POSTS:
            FILE.write(POST + '\n')

# Info
NEW = []

if not os.path.isfile("parsed.txt"):
    update_file()
else:
    MISMATCHES = 0

    FILE = open("parsed.txt", "r")
    LINES = FILE.readlines()
    
    # Remove newlines
    N_LINES = []

    for LINE in LINES:
        N_LINES.append(LINE.replace("\n", "")) 

    for POST in POSTS:
        if not POST in N_LINES:
            MISMATCHES += 1
    
    if DEBUG:
        print(f"MISMATCHES: {MISMATCHES}")

    for MISMATCH in POSTS:
        if POSTS.index(MISMATCH) < MISMATCHES:
            NEW.append(MISMATCH)
    
    if not DEBUG:
        if MISMATCHES > 0:
            update_file()

# Notify
if NEW:
    LEN = len(NEW)

    if LEN > 1:
        send_message(f"🐻 THERE ARE {LEN} NEW POSTS ON THE NEST RUSHERS WEBSITE\n\n*** GO CHECK THEM OUT *** 🐊")

        for POST in NEW:
            send_message(POST)

        send_message("🙏 BIG HOPES THAT YOU WILL ENJOY THEM 🙏")
    else:
        send_message(f"🙉 THERE IS A NEW POST ON THE NEST RUSHERS WEBSITE, CHECK IT OUT: 🥝\n{NEW[0]}")
    

