from flask import Flask, render_template
app = Flask(__name__)

lista = ['Far Cry 3',
         'Valorant',
         'Brawlhalla',
         'Counter Strike',
         'Bloons TD6', 'Stumble Guys',
         'Overcooked 2', 'Life is Strange',
         'Days Gone']



@app.route('/')
def index():
    return 'olá mundo'

@app.route('/games')
def games():
    return render_template('index.html', listaJogo=lista)

if __name__ == '__main__':
    app.run(debug=True)