from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        if num1 is not None and num2 is not None:
            result = num1 + num2
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
