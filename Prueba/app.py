from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    imc = weight / (height ** 2)
    
    if imc < 18.5:
        img = 'underweight.png'
        diagnosis = 'Bajo peso'
    elif 18.5 <= imc < 24.9:
        img = 'normal.png'
        diagnosis = 'Peso normal'
    elif 25 <= imc < 29.9:
        img = 'overweight.png'
        diagnosis = 'Sobrepeso'
    else:
        img = 'obese.png'
        diagnosis = 'Obesidad'
        
    return render_template('result.html', imc=imc, img=img, diagnosis=diagnosis)

@app.route('/diagnosis/<diagnosis>')
def diagnosis_page(diagnosis):
    advices = {
        'Bajo peso': 'Consulta con un nutricionista para una dieta adecuada.',
        'Peso normal': 'Continúa con tu estilo de vida saludable.',
        'Sobrepeso': 'Considera aumentar tu actividad física y vigilar tu dieta.',
        'Obesidad': 'Es recomendable buscar asesoría médica y nutricional.'
    }
    
    return render_template('diagnosis.html', diagnosis=diagnosis, advice=advices[diagnosis])

if __name__ == '__main__':
    app.run(debug=True)

