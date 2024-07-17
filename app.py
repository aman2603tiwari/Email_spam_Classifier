from flask import Flask, request, render_template
import pickle

# Load the model and vectorizer
model = pickle.load(open('model1.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer1.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = vectorizer.transform(data).toarray()
        prediction = model.predict(vect)
        return render_template('results.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
