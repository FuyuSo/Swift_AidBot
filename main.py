from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# التوكن الخاص بك هنا
BOT_TOKEN = "7597137307:AAGS4Y9xVElc-j5pme3cv49gONkhtyxk0d4"

# قاعدة بيانات مبسطة للاختصارات (هنطورها بعدين)
shortcuts = {
    "excel": [
        "Ctrl + Shift + L: Apply/remove filters",
        "Alt + E + S + V: Paste special values only",
        "Ctrl + T: Create table"
    ],
    "chrome": [
        "Ctrl + Shift + T: Reopen closed tab",
        "Ctrl + D: Bookmark page",
        "Ctrl + L: Focus address bar"
    ],
    "word": [
        "Ctrl + B: Bold",
        "Ctrl + I: Italic",
        "Ctrl + U: Underline"
    ],
    "windows": [
        "Win + D: Show desktop",
        "Win + E: Open Explorer",
        "Alt + Tab: Switch window"
    ],
    "obsidian": [
        "Ctrl + P: Command palette",
        "Ctrl + O: Quick open",
        "Ctrl + E: Toggle edit/preview"
    ],
    "notion": [
        "Ctrl + Shift + L: Toggle dark mode",
        "/todo: Add checkbox",
        "/page: Create page"
    ],
    "photoshop": [
        "Ctrl + J: Duplicate layer",
        "B: Brush Tool",
        "Ctrl + Z: Undo"
    ],
    "vs code": [
        "Ctrl + P: Open file",
        "Ctrl + `: Toggle terminal",
        "Alt + ↑ / ↓: Move line"
    ],
    "powerpoint": [
        "F5: Start slideshow",
        "Ctrl + M: New slide",
        "Ctrl + G: Group objects"
    ],
    "youtube": [
        "K: Play/Pause",
        "J / L: Rewind/Forward 10s",
        "M: Mute"
    ]
}

motivations = [
    "ابدأ بحاجة صغيرة، المهم تتحرك!",
    "كل بداية صعبة، بس انت قدها.",
    "جرب تكتب اسم برنامج وسأساعدك باختصاراته 🔧"
]

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك في SwiftAid 🤖\n\nاكتب /help أو اسم برنامج للحصول على اختصاراته!"
    )

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧭 الأوامر:\n"
        "/daily - اختصار عشوائي مفيد\n"
        "/suggest - اطلب اختصارات لبرنامج\n"
        "/feedback - أرسل اقتراح أو رأي\n"
        "\n💬 أو اكتب اسم برنامج مباشرة."
    )

# /daily
async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    key = random.choice(list(shortcuts.keys()))
    choice = random.choice(shortcuts[key])
    await update.message.reply_text(f"📌 {key.title()} Shortcut:\n{choice}")

# /suggest
async def suggest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 اكتب اسم البرنامج وسنضيفه لاحقًا 💡")

# /feedback
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✍️ أرسل أي ملاحظة أو اقتراح وسنعمل عليها 👨‍💻")

# رسائل عادية
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower().strip()
    if msg in shortcuts:
        msg_list = shortcuts[msg]
        reply = f"📚 اختصارات {msg.title()}:\n\n" + "\n".join(f"- {s}" for s in msg_list)
        await update.message.reply_text(reply)
    elif "مش عارف" in msg or "ساعدني" in msg:
        await update.message.reply_text(random.choice(motivations))
    else:
        await update.message.reply_text("🔍 لم أجد اختصارات لهذا البرنامج، جرّب تكتب اسمه بالإنجليزي.")

# تشغيل البوت
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("daily", daily))
app.add_handler(CommandHandler("feedback", feedback))
app.add_handler(CommandHandler("suggest", suggest))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()