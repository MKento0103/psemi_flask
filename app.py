from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    list=["0","1","2","3","4","5","6","7","8","9"]
    dictionary={"好きな色":"緑","好きなゲーム":"VALORANT","好きな本":"同志少女よ，敵を撃て"}
    flag=True
    return render_template('index.html',list=list,dictionary=dictionary,flag=flag)

if __name__ == "__main__":
    app.run(port=8080) 
