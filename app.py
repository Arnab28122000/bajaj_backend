from operator import and_
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import re
import json

app = Flask(__name__)

@app.route("/api/detectObject", methods=["POST"])
@cross_origin(origin='*')
def detectObject():
    req = json.loads(request.data)
    special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
    alphabet = []
    numeric = []
    print(req)
    for arr in req['data']:
        if arr.isnumeric() == False and bool(re.match('^[a-zA-Z0-9]*$', arr)) == True:
            alphabet.append(arr)
        elif arr.isnumeric() == True:
            numeric.append(arr)
    return jsonify({ 
        "is_success": True,
        "user_id": "harsh_raj_1906098",
        "count": len(req['data']),
        "email": "1906098@kkit.ac.in",
        "roll_number": "1906098",
        "numbers": numeric,
        "alphabets": alphabet
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1125, debug=True)
