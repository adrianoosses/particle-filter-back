from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])

def index():
    if request.method == 'POST':
        ##task_content = request.form['content']
        data_postman = request.get_json()

    else:
        return render_template('index.html')

@app.route('/api/get-json')
def hello():
    return jsonify(hello='world')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return jsonify(hello='2')

@app.route('/<username>', methods=['GET', 'POST'])
def show_user(username):
    return jsonify(hello=request.get_json())

if __name__ == "__main__":
    app.run(debug=True)