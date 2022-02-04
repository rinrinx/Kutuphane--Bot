<h1 align="center">
  <b>Cega Maria Soft Bot</b>
</h1>


[![Stars](https://img.shields.io/github/stars/hackertyus/CegaMariaSoft?style=flat-square&color=yellow)](https://github.com/hackertyus/CegaMariaSoft/stargazers)
[![Forks](https://img.shields.io/github/forks/hackertyus/CegaMariaSoft?style=flat-square&color=orange)](https://github.com/hackertyus/CegaMariaSoft/fork)
[![Size](https://img.shields.io/github/repo-size/hackertyus/CegaMariaSoft?style=flat-square&color=green)](https://github.com/hackertyus/CegaMariaSoft/)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/hackertyus/CegaMariaSoft)   
[![Contributors](https://img.shields.io/github/contributors/hackertyus/CegaMariaSoft?style=flat-square&color=green)](https://github.com/hackertyus/CegaMariaSoft/graphs/contributors)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/hackertyus/CegaMariaSoft/blob/main/LICENSE)


## Features

- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Ban, Unban

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used seperated by space )
* Check [info.py](https://github.com/EvamariaTG/evamaria/blob/master/info.py) for more


## Deploy
Bu botu her yerde dağıtabilirsiniz.

<details><summary>Heroku'ya Dağıt</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://heroku.com/deploy">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>VPS'ye Dağıt</summary>
<p>
<pre>
git clone https://github.com/EvamariaTG/evamaria
# Install Packages
pip3 install -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>


## Commands
```
• /log - to get the rescent errors
• /stats - to get status of files in db.
* /deleteall - delete all index(autofilter)
* /sil - delete a specific file from index.
* /info - get user info
* /id - get tg ids.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index  - to add files from a channel
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all Eva Maria users
```

## Credits 
* [![EvaMaria-Devs](https://img.shields.io/static/v1?label=EvaMaria&message=devs&color=critical)](https://telegram.dog/EvaMariaDevs)


## Thanks to 
 - Thanks To EvamariaTG [EvaMaria](https://github.com/EvamariaTG/EvaMaria)
 - Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
 - Thanks To Mahesh For His Awesome [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)
 - Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)
 - Thanks To All Everyone In This Journey

### Note

[Note To A So Called Dev](https://telegram.dog/subin_works/203): 

Kanging this codes and and editing a few lines and releasing a V.x  or an [alpha](https://telegram.dog/subin_works/204), beta , gama branches of your repo wont make you a Developer.
Fork the repo and edit as per your needs.

## Disclaimer
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 2.0.](https://github.com/EvamariaTG/evamaria/blob/master/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.

## Inspiration
This is an attempt to create a clone of a BOAT made out of [banana trees 🌳](https://telegram.dog/GetTGLink/4187)
