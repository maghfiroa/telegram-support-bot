import os
from telegram.ext import CommandHandler, MessageHandler, Filters
from settings import WELCOME_MESSAGE, DAFTAR_HARGA, TELEGRAM_SUPPORT_CHAT_ID, REPLY_TO_THIS_MESSAGE, WRONG_REPLY
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

buttons = [
    [
        InlineKeyboardButton(
            text="Testi VIP NSID 🧾", url="https://t.me/vvipnsid"
        ),
]
]

def start(update, context):
    update.effective_message.reply_photo("https://telegra.ph/file/e2b61fdd83480efe5d49c.jpg",
          WELCOME_MESSAGE, 
          reply_markup=InlineKeyboardMarkup(buttons)) 

    mention = update.message.from_user.mention,
    username = None if not update.message.from_user.username else '@' + message.from_user.username,
    first = update.message.from_user.first_name, 
    id = update.message.from_user.id

    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"""
📞 𝗧𝗲𝗿𝗵𝘂𝗯𝘂𝗻𝗴 : {mention}.
𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}
𝗨𝘀𝗲𝗿 𝗜𝗗 : {id}
        """,
    )

def vip(update, context):
    update.effective_message.reply_photo(
         "https://telegra.ph/file/3ee9d01d99431af443863.jpg",
          """ 🎥LIST GRUP BOK*P TANPA LINK⬇️

1. 🔐VVIP CAMPURAN🔞 = Rp 40.000
✅FULL VIDEO CAMPURAN
✅BERISI BELASAN RIBU VIDEO

2. 🔐VIP RARE 🔞 = Rp 30.000
✅BERISI RIBUAN FULL VIDEO RARE

3. 🔐VIP ONLYFANS 🔞 = Rp 30.000
✅BERISI RIBUAN FULL VIDEO ONLYFANS

4. 🔐VIP HIJAB 🔞 = Rp 30.000
✅BERISI RIBUAN FULL VIDEO HIJAB

5. 🔐VIP LIVE (OME BIGO DLL/VCS) 🔞 = Rp 30.000
✅FULL VIDEO LIVE BIGO OME / VCS

✅BERISI RIBUAN VIDEO
6. 🔐VIP INDO 🔞 = Rp 50.000
✅FULL VIDEO INDO MALAY
✅BERISI BELASAN RIBU VIDEO

7. 🔐VIP JAV 🔞  = Rp 30.000
✅BERISI RIBUAN FULL VIDEO JAV

8.🔐VIP BOCIL 🔞  = Rp 50.000
✅BERISI RIBUAN FULL VIDEO BOCIL

9. 🔐VIP BARAT 🔞  = Rp 30.000
✅BERISI RIBUAN FULL VIDEO BARAT

_berlaku untuk semua grup
✅SEKALI BAYAR PERMANEN
✅DAPAT JAMINAN INVITE ULANG JIKA CH KEBANNED 
✅BEBAS AKSES NO LUAR ATAU INDO
✅UPDATE SETIAP SAAT

🎉JOIN SEMUA GRUP = Rp 200.000

𝙋𝙖𝙮𝙢𝙚𝙣𝙩:
✅DANA(e-money) ✅LINK AJA ✅GOPAY

TESTI DAN JOIN ? : @VVIPNSID

MAU GABUNG? CHAT KE 👇🏻
@ChatJoinVipBot
@ChatJoinVipBot
@ChatJoinVipBot

NB : 
AKUN TIDAK BOLEH DI PRIVASI AGAR MEMUDAHKAN KITA UNTUK MEMBALASNYA!!!""")
          
def forward_to_chat(update, context):
    """{ 
        'message_id': 5, 
        'date': 1605106546, 
        'chat': {'id': 49820636, 'type': 'private', 'username': 'danokhlopkov', 'first_name': 'Daniil', 'last_name': 'Okhlopkov'}, 
        'text': 'TEST QOO', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'username': 'danokhlopkov', 'language_code': 'en'}
    }"""
    forwarded = update.message.forward(chat_id=TELEGRAM_SUPPORT_CHAT_ID)
    if not forwarded.forward_from:
        context.bot.send_message(
            chat_id=TELEGRAM_SUPPORT_CHAT_ID,
            reply_to_message_id=forwarded.message_id,
            text=f'Pesan Dari : {update.message.from_user.mention}'
        )


def forward_to_user(update, context):
    """{
        'message_id': 10, 'date': 1605106662, 
        'chat': {'id': -484179205, 'type': 'group', 'title': '☎️ SUPPORT CHAT', 'all_members_are_administrators': True}, 
        'reply_to_message': {
            'message_id': 9, 'date': 1605106659, 
            'chat': {'id': -484179205, 'type': 'group', 'title': '☎️ SUPPORT CHAT', 'all_members_are_administrators': True}, 
            'forward_from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'danokhlopkov': 'okhlopkov', 'language_code': 'en'}, 
            'forward_date': 1605106658, 
            'text': 'g', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 
            'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
            'from': {'id': 1440913096, 'first_name': 'SUPPORT', 'is_bot': True, 'username': 'lolkek'}
        }, 
        'text': 'ggg', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 
        'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'username': 'danokhlopkov', 'language_code': 'en'}
    }"""
    user_id = None
    if update.message.reply_to_message.forward_from:
        user_id = update.message.reply_to_message.forward_from.id
    elif REPLY_TO_THIS_MESSAGE in update.message.reply_to_message.text:
        try:
            user_id = int(update.message.reply_to_message.text.split('\n')[0])
        except ValueError:
            user_id = None
    if user_id:
        context.bot.copy_message(
            message_id=update.message.message_id,
            chat_id=user_id,
            from_chat_id=update.message.chat_id
        )
    else:
        context.bot.send_message(
            chat_id=TELEGRAM_SUPPORT_CHAT_ID,
            text=WRONG_REPLY
        )


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('vip', vip))
    dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
    dp.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))
    return dp
