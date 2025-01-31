import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Ваш токен, полученный от BotFather
TOKEN = '7580862847:AAHjiyFj05xQui2Dx8ckQd3_eg7cG_K3vV4'

# Список зеркал (замените на реальные ссылки)
mirrors = [
    ("✅ Зеркало 1", "https://t.me/aferiumprobiv_bot"),
    ("✅ Зеркало 2", "https://t.me/aferium_probiv1bot"),
    # Добавьте больше зеркал по необходимости
]

# Текст сообщения
WELCOME_TEXT = """Привет! Лови список актуальных зеркалов пробив бота @aferium

Функционал пробив-ботов:

☎️ Поиск по номеру телефона

🌐 Поиск информации по ссылкам на социальные сети

👤 Поиск по ФИО

ℹ️ Поиск информации по ИНН

🚘 Поиск по номеру автомобиля

📸 Поиск по фотографии

🤑 Помимо обычного использования ты можешь зарабатывать на реферальной системе пригласив своих друзей!

🛠 Если вы обнаружили неисправность, или не работающий бот, пожалуйста напишите мне в лс: @ilya_kowalski
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаем кнопки с зеркалами
    keyboard = [
        [InlineKeyboardButton(text, url=url)] for text, url in mirrors
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с изображением
    with open('welcome.jpg', 'rb') as photo:
        await update.message.reply_photo(photo=photo, caption=WELCOME_TEXT, reply_markup=reply_markup)

def main():
    # Создаем приложение
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler('start', start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
