from flask import Flask, render_template, request
import json


app = Flask(__name__)

@app.route('/test_starwars')
def index():
    global side
    side = 'style.css'
    return render_template('side_choice.html')

@app.route('/main_test')
def show_test():
    global side
    if request.args.get('question-1') == 'светлая':
        side = 'light.css'
        return render_template('test_light.html')
    elif request.args.get('question-1') == 'темная':
        side = 'dark.css'
        return render_template('test_dark.html')
    else:
        return render_template('error.html')

@app.route('/light_test')
def light_test():
    global side
    side = 'light.css'
    return render_template('test_light.html')

@app.route('/dark_test')
def dark_test():
    global side
    side = 'dark.css'
    return render_template('test_dark.html')

@app.route('/end')
def result():
    global side
    print(side)
    answer = []
    for i in range(1, 11):
        answer.append(request.args.get('question-' + str(i)))
    if '' in answer:
        return render_template('error.html', side=side)
    res = [0] * 10
    if side == 'light.css':
        for i in range(10):
            for j in range(10):
                name = light[i]
                ans = int(answer[j])
                res[i] += d[name][j][ans]
        mx = 0
        mx_name = ''
        for i in range(10):
            if res[i] > mx:
                mx = res[i]
                mx_name = light[i]
        for i in range(10):
            res[i] = (res[i], d[light[i]][-2], str(round(res[i] / 40 * 100)) + '%')
        res.sort(reverse=True)
    else:
        for i in range(10):
            for j in range(10):
                name = dark[i]
                ans = int(answer[j])
                res[i] += d[name][j][ans]
        mx = 0
        mx_name = ''
        for i in range(10):
            if res[i] > mx:
                mx = res[i]
                mx_name = dark[i]
        for i in range(10):
            res[i] = (res[i], d[dark[i]][-2], str(round(res[i] / 40 * 100)) + '%')
        res.sort(reverse=True)
    print(res)
    return render_template('res.html', res=res, side=side, file=d[mx_name][-1], name=d[mx_name][-2], text1=dd[mx_name]['info'], text2=dd[mx_name]['personality'])
            

if __name__ == '__main__':
    side = 'style.css'
    light = ['obi-wan', 'anakin', 'chewbacca', 'luke', 'han', 'leia', 'padme', 'c3po', 'r2d2', 'yoda']
    dark = ['palpatine', 'mol', 'vader', 'dooku', 'boba', 'grievous', 'jabba', 'snouk', 'soldier', 'kylo']
    with open('table.json') as file:
        d = json.load(file)
    with open('characters.json') as file:
        dd = json.load(file)
    app.run(port=8080, host='127.0.0.1')
