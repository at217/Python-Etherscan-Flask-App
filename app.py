# save this as app.py
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def results():
    address = request.form['address']
    # data = fetch_data_from_etherscan(address)
    return render_template('results.html')  #return render_template('results.html', data=data)


if __name__=="__main__":
    app.run(debug=True)