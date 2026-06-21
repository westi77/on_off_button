from flask import Flask, jsonify, send_from_directory

# Создаём Flask-приложение
app = Flask(__name__)

# Состояние роборуки — хранится на сервере в памяти
# При перезапуске сервера сбрасывается в False
state = {"powered": False}


# Маршрут: главная страница
# Возвращает файл button.html из той же папки
@app.route("/")
def index():
    return send_from_directory(".", "button.html")


# Маршрут: GET /api/status
# Браузер запрашивает текущее состояние при загрузке страницы
@app.route("/api/status", methods=["GET"])
def get_status():
    return jsonify(state)


# Маршрут: POST /api/toggle
# Браузер отправляет запрос при нажатии кнопки
# Сервер инвертирует состояние и возвращает новое значение
@app.route("/api/toggle", methods=["POST"])
def toggle():
    state["powered"] = not state["powered"]
    print(f"[toggle] Новое состояние: {'ON' if state['powered'] else 'OFF'}")
    return jsonify(state)


if __name__ == "__main__":
    print("Сервер запущен: http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
