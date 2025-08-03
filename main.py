from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    if request.method == 'POST':
        try:
            start = int(request.form['start'])
            end = int(request.form['end'])
            if start > end:
                result = ['Start number must be less than or equal to end number.']
            else:
                result = list(range(start, end + 1))
        except ValueError:
            result = ['Please enter valid numbers.']
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
