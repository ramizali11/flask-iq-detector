from flask import Flask, render_template, request
import numpy as np  

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"]) #method to perform request
def home():
    if request.method == "POST":   #request
        answers = []
        for i in range(1, 11):  #insert the answer from user
            answers.append(int(request.form.get(f"q{i}", 0)))


        correct = np.array([3, 1, 3, 2, 4, 3, 2, 1, 3, 4])  #correct answers
        score = 0
        for i in range(len(correct)):   #check the answer with the help of index 
            if answers[i] == correct[i]:
                score += 1         

        percent = (score / len(correct)) * 100

        iq = score * 10 + 60 

        return render_template("result.html", score=score, percent=percent, iq=iq)   #return the value to result.html

    return render_template("index.html")   #we must return thr requsted template

if __name__ == "__main__":
    app.run(debug=True)
