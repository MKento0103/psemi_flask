from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    list=["0","1","2","3","4","5","6","7","8","9"]
    dictionary={"好きな色":"緑","好きなゲーム":"VALORANT","好きな本":"同志少女よ，敵を撃て"}
    flag=True
    return render_template('index2.html',list=list,dictionary=dictionary,flag=flag)


@app.route("/routing")
def routing():
    return render_template('routing.html')

@app.route('/get',methods=['GET'])
def get():
    request_data=request.args.get('data') 
    print(request_data) 
    return render_template('get.html',request_data=request_data)

@app.route('/post',methods=['POST'])
def post():
    request_data=request.form['data']
    print(request_data) 
    return render_template('post.html',request_data=request_data)

if __name__ == "__main__":
    app.run(port=8080) 