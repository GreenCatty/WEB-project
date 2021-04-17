from flask import Flask, render_template, request
import json


app = Flask(__name__)

@app.route('/test_starwars')
def index():
    return render_template('side_choice.html')

@app.route('/main_test')
def show_test():
    if request.args.get('question-1') == 'светлая':
        return render_template('test_light.html')
    elif request.args.get('question-1') == 'темная':
        return render_template('test_dark.html')
    else:
        return render_template('error.html')

@app.route('/light_test')
def light_test():
    return render_template('test_light.html')

@app.route('/dark_test')
def dark_test():
    return render_template('test_dark.html')

@app.route('/end_light')
def result_light():
    answer = []
    for i in range(1, 11):
        answer.append(request.args.get('question-' + str(i)))
    if '' in answer:
        return render_template('error_light.html')
    res = [0] * 10
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
    print(res)
    return render_template('res_light.html', file=d[mx_name][-1], name=d[mx_name][-2], text1=dd[mx_name]['info'], text2=dd[mx_name]['personality'])


@app.route('/end_dark')
def result_dark():
    answer = []
    for i in range(1, 11):
        answer.append(request.args.get('question-' + str(i)))
    if '' in answer:
        return render_template('error_dark.html')
    res = [0] * 10
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
    print(res)
    return render_template('res_dark.html', file=d[mx_name][-1], name=d[mx_name][-2], text1=dd[mx_name]['info'], text2=dd[mx_name]['personality'])
            



if __name__ == '__main__':
    light = ['obi-wan', 'anakin', 'chewbacca', 'luke', 'han', 'leia', 'padme', 'c3po', 'r2d2', 'yoda']
    dark = ['palpatine', 'mol', 'vader', 'dooku', 'boba', 'grievous', 'jabba', 'snouk', 'soldier', 'kylo']
    with open('table.json') as file:
        d = json.load(file)
    with open('characters.json') as file:
        dd = json.load(file)
    app.run(port=8080, host='127.0.0.1')
