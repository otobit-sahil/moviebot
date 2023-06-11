class script(object):
    START_TXT = """<b>👋 Hello {},

I Can Provide Movies And Series, Just Add Me In Your Group And Make Me Admin!!

🔅 Powered by: @Movies7x</b>
"""
    HELP_TXT = """<b>𝖧𝖾𝗅𝗅𝗈 𝖬𝗋. {} 𝖨𝗍'𝗌 𝖬𝗒 𝖧𝖾𝗅𝗉 𝖬𝗈𝖽𝗎𝗅𝖾</b>"""

    ABOUT_TXT = """<b>✯ Mʏ Nᴀᴍᴇ : {}</b>

<b>✯ Cʜᴀɴɴᴇʟ : @Movies7x</b>

<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ5.0.1 [Sᴛᴀʙʟᴇ]</b>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Movies7x)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features 

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all connected groups</code>
• /dellfiles - <code>to delete specific name files form the database</code>"""

    STATUS_TXT = """𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌: <code>{}</code>
𝖳𝗈𝗍𝖺𝗅 𝖬𝖾𝗆𝖻𝖾𝗋𝗌: <code>{}</code>
𝖳𝗈𝗍𝖺𝗅 𝖢𝗁𝖺𝗍𝗌: <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾: <code>{}</code>
 """
    PRIVATEBOT_TXT = """<b>ʜᴇʟʟᴏ {}, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ.

ɪ'ᴍ ᴊᴜsᴛ ᴀ sɪᴍᴘʟᴇ ᴘʀᴇ-ғᴜɴᴄᴛɪᴏɴᴇᴅ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʙᴏᴛ.

ɪᴛ's ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ.</b>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    IMDB_TEMPLATE_TXT = """<i><b>📟 Movie Name</b></i> : <i><b><a href={url}>{title}</a></b></i>
<i><b>🗒️ Release Date</b></i> : <i><b>{release_date}</b></i>

<i><b>⭐ IMDB Rating</b></i> : <i><b><a href={url}/ratings>{rating}/10</a></b></i>
<i><b>🎞️ Genres</b></i> : <i><b>{genres}</b></i>

<i><b>👩🏻‍💻 Requested By</b></i> : <i><b>{message.from_user.mention}</b></i>
<i><b>🚀 Group</b></i> : <i><b>{message.chat.title}</b></i>"""

    VERIFED_TXT = """<b>ʜᴇʟʟᴏ {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀғɪᴇᴅ ғᴏʀ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ,
ᴇɴᴊᴏʏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ...</b>"""

    VERIFY_TXT = """<b>ʜᴇʟʟᴏ {},

ʏᴏᴜʀ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ,
ᴘʟᴇᴀꜱᴇ ᴠᴇʀɪғʏ ɴᴏᴡ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ...

इस बाॅट को इस्तेमाल करने के लिए आपको ᴠᴇʀɪғʏ करना होगा नहीं तो आप इसका इस्तेमाल नहीं कर पाएंगे |</b>"""

    VERIFY2_TXT = """
<b>#𝖴𝖲𝖤𝖱_𝖵𝖤𝖱𝖨𝖥𝖨𝖤𝖣_𝖢𝖮𝖬𝖯𝖫𝖤𝖳𝖤

𝖴𝗌𝖾𝗋 𝖭𝖺𝗆𝖾 : {} [ <code>{}</code> ]

𝖣𝖺𝗍𝖾  : <code>{}</code></b>
"""
