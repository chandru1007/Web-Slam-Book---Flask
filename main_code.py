from flask import *

app=Flask(__name__)

@app.route("/slam_home")
def slam_home():
    return render_template("slam_home.html")

@app.route("/name")
def name():
    return render_template("name.html")

@app.route("/buddy")
def buddy():
    return render_template('buddy.html')

@app.route("/display",methods = ["POST","GET"])
def display():
    if request.method == "POST":
        dat={}
        dat['input1']      =   request.form['input1']
        dat['input2']      =   request.form['input2']
        dat['input3']      =   request.form['input3']
        dat['input4']      =   request.form['input4']
        dat['input5']      =   request.form['input5']
        dat['input6']      =   request.form['input6']
        dat['input7']      =   request.form['input7']
        dat['input8']      =   request.form['input8']
        dat['input9']      =   request.form['input9']
        dat['input10']     =   request.form['input10']
        dat['input11']     =   request.form['input11']
        dat['input12']     =   request.form['input12']
        dat['input13']     =   request.form['input13']
        return render_template('display.html',rec = dat)

if __name__ == "__main__":
    app.run(debug=True)
