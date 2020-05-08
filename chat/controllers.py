from aplicacao import app
from flask import render_template

@app.route('/')
def index():
    context = {'titulo': 'Página Principal', 'mensagens': ['Usuario1: Olá', 'Usuario2: Oi']}
    return render_template('index.html', **context)

app.run(debug=True)
