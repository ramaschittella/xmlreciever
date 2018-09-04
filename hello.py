from flask import Flask
from SPARQLWrapper import SPARQLWrapper, JSON
app = Flask(__name__)

@app.route('/')
def hello_world():
	sparql = SPARQLWrapper("http://localhost:3030/BookMashup/query")
	sparql.setQuery("""
		PREFIX rdfs: <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>
		SELECT ?label
		WHERE { <http://dbpedia.org/resource/120_Days_of_Sodom> rdfs:label ?label }
	""")
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	
	for result in results["results"]["bindings"]: 
                print(result["label"]["value"])
	        
