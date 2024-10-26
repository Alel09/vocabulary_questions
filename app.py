from flask import Flask, request, render_template
import random

app = Flask(__name__)

preguntas = {
    "grade": "calificacion",
    "embassy": "embajada",
    "tour": "recorrer",
    "raise": "criar",
    "fit fit fit": "ajustar",
    "fitting room": "probador",
    "full time": "tiempo completo",
    "part time": "medio tiempo",
    "borrow": "pedir prestado",
    "loan": "prestamo",
    "advice": "consejo",
    "advise": "aconsejar",
    "luggage": "equipaje",
    "suit case": "maleta",
    "briefcase": "portafolio",
    "trust": "confiar",
    "trunk": "cajuela",
    "nearby": "cercano",
    "pond": "estanque",
    "outdoor": "al aire libre",
    "indoor": "en interiores",
    "diaper": "pañal",
    "dig dog dog": "cabar",
    "shover": "pala",
    "axe": "hacha",
    "patient": "paciente",
    "patience": "paciensia",
    "springwater": "valniario",
    "sea food": "mariscos",
    "meat": "carne",
    "relative": "pariente",
    "rotten": "podrido",
    "fire": "despedir",
    "hire": "contratar",
    "brag": "presumir",
    "be have": "comportarse",
    "say a toast": "brindar",
    "stranger": "extraño",
    "homeless": "indigente",
    "handicapped": "discapacitado",
    "insurance": "seguro",
    "be ashamed": "estar apenado",
    "fluent": "fluido",
    "success": "exito",
    "avoid": "evitar",
    "give up gave up given up": "darse por vencido",
    "be asleep": "estar durmiendo",
    "run out of (someting)": "quedarse sin algo",
    "weapon": "arma",
    "stroller": "carriola",
    "pulled beef": "res desebrada",
    "pulled chicken": "pollo desebrado",
    "pulled pork": "puerco desebrado",
    "boiled egg": "huevos cocidos",
    "chocolate bar": "barra de chocolate",
    "meal": "comida del dia",
    "get along with": "llevarse bien",
    "fence": "reja",
    "clawl": "gatear",
    "reply": "contestar"
}

@app.route('/', methods=['GET', 'POST'])
def examen():
    if request.method == 'POST':
        respuestas = request.form.to_dict()
        puntaje = sum(1 for i, pregunta in enumerate(preguntas.items()) if respuestas[f"pregunta_{i}"].lower() == pregunta[1].lower())
        total_preguntas = len(preguntas)
        return render_template('resultado.html', puntaje=puntaje, total_preguntas=total_preguntas)
    else:
        preguntas_random = list(preguntas.items())
        random.shuffle(preguntas_random)
        return render_template('index.html', preguntas=preguntas_random)

if __name__ == '__main__':
    app.run(debug=True)
