import os

from flask import Flask, request, abort

from exception import ApiError
from utils import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    cmd_1 = request.args.get('cmd_1')
    val_1 = request.args.get('val_1')
    cmd_2 = request.args.get('cmd_2')
    val_2 = request.args.get('val_2')
    file_name = request.args.get('file_name')

    if not(cmd_1 and val_1 and file_name):
        abort(400)

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400, 'Wrong fileparth')

    with open(file_path) as file:
        try:
            res = build_query(cmd_1, val_1, file)
            if cmd_2 and val_2:
                res = build_query(cmd_2, val_2, res)
            res = '\n'.join(res)
        except (ValueError, TypeError):
            raise ApiError('Value is Not Int or Wrong Command')

    return app.response_class(res, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
