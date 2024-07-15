from flask import Flask, render_template

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
