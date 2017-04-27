from chalice import Chalice

app = Chalice(app_name='chalice-test')


@app.route('/ping', methods=['GET'])
def index():
    return {'a':'pong'}

