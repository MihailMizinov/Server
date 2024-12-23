from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)

# Инициализация Swagger
swagger = Swagger(app)

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    """
    Получить расписание
    ---
    responses:
      200:
        description: Список расписаний
        schema:
          type: array
          items:
            type: object
            properties:
              day:
                type: string
                example: Понедельник
              subject:
                type: string
                example: Математика
    """
    # Пример данных для API
    schedule = [
        {"day": "Понедельник", "subject": "Математика"},
        {"day": "Вторник", "subject": "Физика"},
        {"day": "Среда", "subject": "Химия"},
        {"day": "Четверг", "subject": "История"},
        {"day": "Пятница", "subject": "Биология"}
    ]
    return jsonify(schedule)

if __name__ == '__main__':
    app.run(debug=True)
