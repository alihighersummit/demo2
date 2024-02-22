from flask import Flask, render_template, request
from database.user import User
from flask import jsonify
from constant import Constants
app = Flask(__name__)


@app.route('/')
def roots():
   value = User.get_user()
   return render_template('index.html')

@app.route('/s', methods=['POST'])
def root():
   value = User.get_user()
   name = request.form.get('username')
   return render_template('index.html', name=name, lis=value)

if __name__ == '__main__':
   app.run(debug=False, host=Constants.REST_SERVER_API_ADDRESS, port=Constants.REST_SERVER_PORT)
