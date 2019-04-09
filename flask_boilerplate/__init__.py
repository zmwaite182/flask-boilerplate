from flask import Flask, request, make_response, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/hello')
    def hello():
        name = request.args.get('name', 'World')
        return render_template('hello.html', name=name)

    @app.route('/number/<int:n>')
    def number_route(n):
        return f'Number: {n}'


    @app.route('/calculate', methods=['GET', 'POST'])
    def calculate():
        result = None
        operator = '+'

        if request.method == "GET":
            return render_template('calculate.html', action="Add")
        if request.method == "POST":
            x = int(request.form['x'])
            y = int(request.form['y'])
            action = request.form['action']

            if action == "Add":
                result = x + y
            if action == "Subtract":
                operator = '-'
                result = x - y
            if action == "Multiply":
                operator = '*'
                result = x * y
            if action == "Divide":
                operator = '/'
                result = x / y

            return render_template("calculate.html", result=result, x=x, y=y, action=action, operator=operator)


    method_route_allows = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']

    @app.route('/method', methods=method_route_allows)
    def method_route():
        method = request.method
        return render_template('methods.html', method=method, methods=method_route_allows)

    @app.route('/status')
    def status_route():
        code = request.args.get('c', 200)
        response = make_response("", code)
        return response


    return app
