from flask import Flask ,request,jsonify
app=Flask(__name__)

@app.route("/v1/sanitized/input/<string:name>")
def my_method(name:str):
    #name=request.args.get("name")
    if name is None:
      return jsonify(result="unsanitized"),200
    else:
      return jsonify(result="sanitized"),200
if __name__=="__main__":
    app.run(debug=True)
    
    
#this API is successfully works & tested with POSTMAN PAYLOAD 