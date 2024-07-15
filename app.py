from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/situacaofinal/<float:nota>')
def situacaofinal(nota):
    if nota < 30:
        return 'Reprovado'
    elif nota >= 60:
        return 'Aprovado'
    else:
        return 'Em recuperação'

@app.route('/arearestrita/<admin>')
def arearestrita(admin):
    if admin=='sim':
        return render_template('admin.html')
    else:
        return render_template('comum.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificalogin')
def verificalogin():
    login = request.form['login']
    senha = request.form['senha']

    if login=='alba' and senha='12345':
        return render_template('admim.html')
    else:
        return 'Login ou senha incorretos'