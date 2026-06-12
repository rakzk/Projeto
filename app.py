from flask import Flask, render_template, request

app = Flask(__name__)

questoes = [

    # MATEMÁTICA

    {
        "pergunta": "Quanto é 5 + 3?",
        "alternativas": ["6", "7", "8", "9"],
        "correta": "8"
    },
    {
        "pergunta": "Quanto é 10 x 2?",
        "alternativas": ["20", "15", "18", "22"],
        "correta": "20"
    },
    {
        "pergunta": "Quanto é 12 ÷ 4?",
        "alternativas": ["2", "3", "4", "5"],
        "correta": "3"
    },
    {
        "pergunta": "Quanto é 25 - 8?",
        "alternativas": ["15", "16", "17", "18"],
        "correta": "17"
    },
    {
        "pergunta": "Qual é o dobro de 9?",
        "alternativas": ["16", "17", "18", "19"],
        "correta": "18"
    },

    # PORTUGUÊS

    {
        "pergunta": "Qual destas palavras é um substantivo?",
        "alternativas": ["Correr", "Bonito", "Escola", "Rapidamente"],
        "correta": "Escola"
    },
    {
        "pergunta": "Qual é o plural de 'animal'?",
        "alternativas": ["Animais", "Animales", "Animãos", "Animaises"],
        "correta": "Animais"
    },
    {
        "pergunta": "Qual destas palavras é um verbo?",
        "alternativas": ["Mesa", "Feliz", "Estudar", "Caneta"],
        "correta": "Estudar"
    },
    {
        "pergunta": "Qual é o antônimo de 'alto'?",
        "alternativas": ["Grande", "Baixo", "Largo", "Forte"],
        "correta": "Baixo"
    },
    {
        "pergunta": "Em qual palavra a sílaba tônica está destacada corretamente?",
        "alternativas": ["CA-sa", "bo-LA", "ja-NE-la", "es-CO-la"],
        "correta": "ja-NE-la"
    }
]
   

@app.route('/')
def index():
    return render_template('index.html', questoes=questoes)

@app.route('/resultado', methods=['POST'])
def resultado():

    pontos = 0

    for i, questao in enumerate(questoes):
        resposta = request.form.get(f'questao{i}')

        if resposta == questao['correta']:
            pontos += 1

    percentual = (pontos / len(questoes)) * 100

    return render_template(
        'resultado.html',
        pontos=pontos,
        total=len(questoes),
        percentual=percentual
    )

if __name__ == '__main__':
    app.run(debug=True)
    