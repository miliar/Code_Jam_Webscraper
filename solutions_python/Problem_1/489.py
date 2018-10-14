# -*- coding: utf-8 -*-
import os
import sys


# Auxiliar Functions

def resetearMarcados(engines):
	marcados = dict()
	for engine in engines:
		marcados[engine] = False
	return marcados

def cantidadEnTrue(marcados):
	n = 0
	for engine in marcados.keys():
		if marcados[engine] == True:
			n = n + 1
	return n



# Main

inputFile = open('A-large.in', 'r')
nCases = int(inputFile.readline().strip())

for case in range(nCases):
	
	nEngines = int(inputFile.readline().strip())
	engines = []
	for engine in range(nEngines):
		engines.append(inputFile.readline().strip())
	
	nQueries = int(inputFile.readline().strip())
	queries = []
	for query in range(nQueries):
		queries.append(inputFile.readline().strip())

#	print 'Case #' + str(case)
#	print 'engines: ' + str(engines)
#	print 'queries: ' + str(queries)

	marcados = resetearMarcados(engines)
	
	switches = 0
	
	for query in queries:
		marcados[query] = True
		if cantidadEnTrue(marcados) == len(engines):
			switches = switches + 1
			marcados = resetearMarcados(engines)
			marcados[query] = True
	
	print 'Case #' + str(case + 1) +': ' + str(switches)




