from flask import Flask
from flask import request
from flask import jsonify
from BudaApi.BudaHMACAuth import BudaHMACAuth
import requests.auth
import requests
import json
import os
from BudaApi.pow import BudaProof
from dotenv import load_dotenv
from flask import Flask, current_app
load_dotenv()
apiKey = os.getenv('BUDA_API_KEY')
secretKey = os.getenv('BUDA_SECRET_KEY')
buda=BudaHMACAuth(apiKey, secretKey)

app = Flask(__name__)
@app.route('/')
def getIndex():
    return current_app.send_static_file('index.html')
    

@app.route("/addOrder", methods=["POST"])
def addOrder():
    try:
        market_id = 'btc-clp'
        url = f'https://www.buda.com/api/v2/markets/{market_id}/orders'
       # auth = BudaHMACAuth(api_key, secret)
        response = requests.post(url, auth=buda, json={
            'type': 'Bid',
            'price_type': 'limit',
            'limit': 1000000,
            'amount': 0.05,
        })
        print(response.json())
    except:
        print("An exception occurred")
    return response.json()

@app.route("/balances")
def balances():

    try:
        
        # buda.get_nonce()
        # buda.sign()
        # buda.__call__()
        #print(buda.api_key)
        request = requests.get("https://www.buda.com/api/v2/balances", auth=buda)
        if request.status_code == requests.codes.ok:
            print(request.headers['content-type'])
            print(request.json())
            print("aca")
        else:
            print("no")
    except:
        print("An exception occurred")
    
    return request.json()

@app.route("/orders")
def orders():
    try:
        market_id = 'btc-clp'
        url = f'https://www.buda.com/api/v2/markets/{market_id}/orders'
        response = requests.get(url, auth=buda, params={
            'state': 'pending',
            'per': 20,
            'page': 1,
        })
        print(response.json())
    except:
        print("An exception occurred")
    
    return response.json()

@app.route("/withdrawals")
def withdrawals():
    try:
        currency = 'btc'
        url = f'https://www.buda.com/api/v2/currencies/{currency}/withdrawals'

        response = requests.post(url, auth=buda, json={
            'amount': 0.05,
            'simulate': True,
            'amount_includes_fee': True,
            'withdrawal_data': {
                'target_address': 'mo366JJaDU5B1hmnPygyjQVMbUKnBC7DsY',
            },
        })
        print(response.json())
    except:
        print("An exception occurred")
    
    return response.json()

"""
@api {get} /simulate Simula transaction via unarequest POST a mi cuenta de Buda.com
@apiName simulate
@apiGroup simulate

@apiSuccess {Object} response La respuesta de POST https://www.buda.com/api/v2/currencies/clp/deposits

"""
@app.route("/simulate", methods=["GET"])
def simulateFound():
    currency = 'clp'
    url = f'https://www.buda.com/api/v2/currencies/{currency}/deposits'
    response = requests.post(url, auth=buda, json={
        'simulate': True,
        'amount': 25000,
    })
    return(response.json())
"""

@apiName proofOfBuda
@apiGroup proofOfBuda
@api {get} /proofOfBuda?text=SomeText Default text is "b00da"

@queryParam  {String} un texto para calcular el proof of work
@apiSuccess {Object} text        Un objeto con el hash ,el text y nonce.

"""
@app.route('/proofOfBuda', methods=['GET'])
def proofOfBuda():
    text = request.args.get('text')
    if not text:
        text='b00da'
    prueba= BudaProof(text)
    #pow.start()
    # print(prueba.pown())
    print(prueba.pown())
    response=prueba.pown()
    return jsonify(response)

