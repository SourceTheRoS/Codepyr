from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

By @nnn_e
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("‹ بدء استخراج جلسة ›", callback_data="generate")],
        [InlineKeyboardButton(text="‹ الصفحة الرأيسية ›", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("‹ بدء استخراج جلسة ›", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("‹ بدء استخراج جلسة ›", callback_data="generate")],
        [InlineKeyboardButton(". WolveS .", url="https://t.me/nnn_e")],
        [
            InlineKeyboardButton("‹ طريقة الاستخدام ›", callback_data="help"),
            InlineKeyboardButton("‹ حول البوت ›", callback_data="about")
        ],
        [InlineKeyboardButton(". WolveS .", url="https://t.me/nnn_e")],
    ]

    # Help Message
    HELP = """
✨ **اوامر البوت** ✨

/about - حول البوت
/help - المساعدة
/start - بدء
/generate - بدء استخراج جلسة
/cancel - 
/restart - اعادة تشغيل
"""

    # About Message
    ABOUT = """
**حول البوت** 

- بوت يقوم باستخراج جلسة تيليثون (كود تيرمكس) و جلسة بايروقرام .

[WolveS](https://t.me/nnn_e)


    """
