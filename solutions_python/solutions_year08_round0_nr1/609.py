#!/bin/python
import os
import time
def analise (engine,queries,dic_q,dic_e):
	num = len(engine)
	trecho = 0
	for i in range(len(queries)):
		#print "%s %s %d" %(queries[i].__str__(),dic_q [queries[i].__str__()],num)
		if dic_q [queries[i].__str__()] >= 1:
			dic_q [queries[i].__str__()] += 1
		else:
			dic_q [queries[i].__str__()] = 1
			num -= 1
		if (num == 0):
			#max = 0 
			if (i != (len(queries))):
				trecho += 1
			del dic_q
			dic_q = {}.fromkeys(queries)
			dic_q [queries[i].__str__()] = 1
			num = len(engine)-1
			#for str in queries:
			#	if dic_q[str.__str__()] > max:
			#		max = dic_q[str.__str__()]
			#		name 

	return trecho

k =  raw_input("")
num_test = int(k)
num_final = num_test
n = 1
resposta = []
#print "k = %d"%(num_test)
while num_test > 0 :
	engine = []
	num_engine = raw_input("")
	#print num_engine
	k = int(num_engine)
	for i in range(k):
		engine.append(raw_input(""))

	queries = []
	num_queries = raw_input("")
	dic_e = {}.fromkeys(queries)

	k = int(num_queries)
	for i in range(k):
		queries.append(raw_input(""))

	dic_q = {}.fromkeys(queries)

	resposta.append( analise (engine,queries,dic_q,dic_e))
	num_test -= 1
	n -= 1
	del dic_q
	del dic_e
	#t= raw_input("wait")
	#time.sleep(4000)
for i in range(num_final):
	print "Case #%d:"% (i+1),resposta[i]


