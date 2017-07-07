from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    if session.get('gold') == None and session.get('activities') == None:
        session['gold'] = 0
        session['activities'] = []
    
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process():
    buildingVisited = request.form['building']
    if buildingVisited == 'farm':
        dGold = random.randrange(10, 21)
    elif buildingVisited == 'cave':
        dGold = random.randrange(5, 11)
    elif buildingVisited == 'house':
        dGold = random.randrange(2, 6)
    elif buildingVisited == 'casino':
        dGold = random.randrange(-50, 51)
    session['gold'] += dGold
    if session['gold'] < 0:
        session['gold'] = 0

    if dGold >= 0:
        activitiesStr = 'Earned '
        color = 'green'
    else:
        activitiesStr = 'Lost '
        color = 'red'
    activitiesStr += str(abs(dGold)) + ' gold(s) '
    activitiesStr += 'from the ' + buildingVisited + '!\n'
    activitiesTuple = (activitiesStr, color)
    session['activities'].insert(0, activitiesTuple)

    return redirect('/')


app.run(debug=True)