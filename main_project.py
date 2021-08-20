from flask import Flask, json, jsonify, request
app = Flask(__name__)

@app.route('/v1/sanitized/input/<payload>', methods=['POST'])
def mymethod(payload):
    data = json.loads(request.data)
    payload = data.get("text",None)
    if payload is None:
        return jsonify({"result ":"unsanitized"})
    else:
        return ({"result":"sanitized"})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
    
#this approach might give error  sometimes that method can't find i am not aware about how to rectify it