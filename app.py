import requests
from flask import Flask, render_template,request,redirect,url_for
import os
import json

app = Flask(__name__)
URL_BASE="https://phonevalidation.abstractapi.com/v1/"
URL_BASE2="https://pokeapi.co/api/v2/pokemon-form/"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact')
def contacto():
    return render_template("contact.html")

@app.route('/about')
def sobre_nosotros():
    return render_template("about.html")

@app.route('/movil',methods=["POST"])
def movil():
    key=os.environ["api_key"]
    print ("Formato valido: pefijo+numero; Ej:34123456789")
    phone= []
    telf=request.form.get("telf")
#    phone1= []
    payload = {'api_key':key , 'phone':telf}
    print (payload)
    #payload1 = {'phone':phone1}
    r=requests.get(URL_BASE,params=payload)
    print (r)
    #r2=requests.get(URL_BASE2+payload1)
    if r.status_code == 200:
        doc=r.json()
        dict={"Telefono":doc.get("format").get("local"), "Valido":doc.get("valid")}
        print ("Esto es el dicionario", dict)
        phone.append(dict)
        print ("Esto es la lista",phone)
        #if r2.status_code == 200:
        #    doc2=r2.json()
    #    print("Id:",doc2.get("id"))
    #    print("Pokemon:",doc2.get("name"))
    #    print("Sprite:",doc2.get("sprites").get("front_default"))
    #    print("Tipo:",doc2.get("types")[0].get("type").get("name"))
        #print ("Error, el telefono no es valido")
        return render_template("movil.html", phone=phone)

#port=os.environ["PORT"]
#app.run("0.0.0.0",int(port),debug=True)
app.run("0.0.0.0",debug=True)