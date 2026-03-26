import os
from flask import Flask, render_template, request

# Настройка путей
template_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(template_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

# ТВОИ УСЛУГИ (ОБНОВЛЕННЫЕ)
SERVICES = [
    {
        "title": "Копирайтинг Pro",
        "desc": "20 лет опыта (с 2006 г.). Создаю продающие смыслы: от лендингов до сложных SEO-стратегий.",
        "icon": "bi-pen-fill"
    },
    {
        "title": "WB & Ozon",
        "desc": "Дизайн карточек с инфографикой. Повышаю CTR и выделяю ваш товар среди тысяч конкурентов.",
        "icon": "bi-shop-window"
    },
    {
        "title": "IT-Разработка",
        "desc": "Умные Telegram-боты и Android-приложения на Python (Kivy). Автоматизация вашего бизнеса.",
        "icon": "bi-cpu-fill"
    },
    {
        "title": "3D & Дизайн",
        "desc": "Параметрическое моделирование кодом Python. Оформление Twitch-каналов и брендинг.",
        "icon": "bi-box-seam"
    }
]

@app.route('/')
def index():
    return render_template('index.html', services=SERVICES)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    contact_info = request.form.get('contact')
    return f"""
    <div style="text-align: center; padding: 50px; font-family: sans-serif;">
        <h1>Спасибо, {name}!</h1>
        <p>Заявка принята. Я свяжусь с вами по контакту: <b>{contact_info}</b></p>
        <br>
        <a href="/">Вернуться на главную</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True)