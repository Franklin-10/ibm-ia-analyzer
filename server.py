"""
Modulo de servidor Flask
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_emotion():
    """
    Rota que recebe o texto e retorna a emoção dominante
    """
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    response = emotion_detector(text_to_analyze)
    if response is None or response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # 4. Formatação obrigatória contendo TODOS os scores individuais
    formated = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formated

@app.route("/")
def render_index_page():
    """
    Rota pagina index
    """
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
