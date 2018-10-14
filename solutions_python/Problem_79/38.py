import string
import math


def make_dic ( word ):
	dic = {}
	for i in xrange(len(word)):
		if not dic.has_key(word[i]): dic[word[i]] = [i];
		else: dic[word[i]].append(i)
	return dic

def joga (word, letras, dic, esquemas, wi):
	s = 0
	maxi = 0
	#print '---------------',word
	for i in word: maxi = max(max,word.find(i))
	play = [True]*len(dic)
	
	for j in xrange(len(dic)):
		if len(dic[j]) != len(word): play[j] = False
	
	for i in xrange(len(letras)):
		
		#procura palavra que tem a proxima letra
		achou = 0
		letra = letras[i]
		for j in xrange(len(dic)):
			if not play[j]: continue
			if esquemas[j].has_key(letra):
				achou = 1;
				break;
		
		if achou == 0: continue
		#print letra
		if not letra in word:
		#	print '>>',letra
			s += 1
			for j in xrange(len(dic)):
				if dic[j] == word or play[j] == False: continue
				if letra in dic[j]: play[j] = False
			continue
		
		gabarito = esquemas[wi][letra]
		#elimino quem nao eh igual a palavra
		for j in xrange(len(dic)):
			if play[j] == False or play[j] == word: continue
			if len(dic[j]) != len(word): play[j] = False
			elif not esquemas[j].has_key(letra) or  esquemas[j][letra] != gabarito: play[j] = False
		
		#print 'letra,achou',letra,achou,play,dic	
		if letra not in word: s += achou
	
	#print 'soma...',s
	return s
	

t = input('')
for cases in xrange(0,t):
	line = raw_input("").split(' ')
	n = int(line[0]); m = int(line[1])
	dic = [0]*n; lista = [0]*m; esquemas = [0]*n
	for i in xrange(n): dic[i] = raw_input("")
	for i in xrange(m): lista[i] = raw_input("")
	
	for i in xrange(n): esquemas[i] = make_dic(dic[i])
	#print esquemas
	
	print 'Case #%d:' % (cases+1),
	for i in xrange(m):
		best = 0; poder = joga(dic[0],lista[i],dic,esquemas,0)
		for j in xrange(1,n):
			aux = joga(dic[j],lista[i],dic,esquemas,j)
			if aux > poder: best = j; poder = aux;
		print dic[best],
	print '\n',
	
	#print dic, lista
