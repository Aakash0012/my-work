from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def indexx():
    h=[]
    table = (request.args.get('table'))
    print(table)
    if table==None:
        table=5
    else:
        table=int(table)

    for i in range(1, 11):
        h.append(i*table)
    return render_template('indexx.html', h=h)

@app.route('/table', methods=['POST', 'GET'])
def table():
    import requests 
    h=[]
    table = int(request.form['table'])

    for i in range(1, 11):
        h.append(i*table)
    return render_template('indexx.html', h=h)

@app.route('/geet')
def geet():
    return render_template('geet.html')

@app.errorhandler(414)
def page_not_found(e):
    return ( render_template('414.html'), 414 )

if __name__ == '__main__':
    app.run(debug=True)