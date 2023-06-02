from flask import Flask, render_template

app = Flask (__name__)

entradas = [
    {
        'titulo':  'Primeiro Post do Blog',
        'texto' : 'Primeiro texto'
    },
    {
        'titulo': 'Segundo Post do Blog',
        'texto' : 'Segundo texto'
    }
]

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas = entradas)