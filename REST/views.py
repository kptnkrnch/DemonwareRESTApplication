from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import MySQLdb
import MySQLdb.cursors

def EstablishConnection():
	db = MySQLdb.connect("192.168.1.34", "root", "root", "Demonware")
	return db

# Create your views here.
@api_view(['GET', 'POST'])
def retrieveOrCreate(request, format=None):
	"""
	Lists (GET) or creates (POST)
	"""
	cursor = None
	db = None
	if db == None:
		db = EstablishConnection()
	
	cursor = db.cursor()
	#data = cursor.fetchone()
	#print("Database version : %s " % data)
	
	if request.method == 'GET':
		cursor.execute("SELECT * FROM CallOfDuty;")
		data = cursor.fetchall()
		lst = []
		for item in data:
			json = "{'id':'%s', 'name':'%s', 'year':'%s', 'score':'%s'}" % (str(item[0]), str(item[1]), str(item[2]), str(item[3]))
			lst.append(json)
			print(json)
		db.close()
		return Response(lst, status=status.HTTP_201_CREATED)
	elif request.method == 'POST':
		querystring = "INSERT INTO CallOfDuty (name, year, score) VALUES ('" + request.data['name'] + "', " + request.data['year'] + ", " + request.data['score'] + ");"
		cursor.execute(querystring)
		db.commit()
		print(querystring)
	
	db.close()
	return Response("HELLO WORLD")
	
@api_view(['GET', 'PUT', 'DELETE'])
def retrieveUpdateOrDelete(request, pk, format=None):
	"""
	Retrieves a single entry (GET using pk for primary key), updates (PUT), or deletes (DELETE)
	"""
	cursor = None
	db = None
	if db == None:
		db = EstablishConnection()
	
	cursor = db.cursor()
	
	if request.method == 'GET':
		cursor.execute("SELECT * FROM CallOfDuty WHERE id=%s;" % pk)
		item = cursor.fetchone()
		json = "{'id':'%s', 'name':'%s', 'year':'%s', 'score':'%s'}" % (str(item[0]), str(item[1]), str(item[2]), str(item[3]))
		db.close()
		return Response(json, status=status.HTTP_201_CREATED)
	elif request.method == 'PUT':
		querystring = "UPDATE CallOfDuty SET name = '" + request.data['name'] + "', year = " + request.data['year'] + ", score = " + request.data['score'] + " WHERE id=%s;" % pk
		cursor.execute(querystring)
		db.commit()
	elif request.method == 'DELETE':
		querystring = "DELETE FROM CallOfDuty WHERE id=%s;" % pk
		cursor.execute(querystring)
		db.commit()
	return Response("Hello world")
