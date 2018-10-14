import re
import math
import numpy as np
import string
from decimal import *

##########################################################################################################################

def parseInputData(problem, s_input, s_id):
	finput = open(problem + '-' + s_input + '-' + s_id + '.in','r')
	nCase = int(finput.readline().strip())
	inputList = finput.readlines()	
	finput.close()
	return nCase, inputList

##########################################################################################################################

def writeOutput(result, problem, s_input, s_id):
	foutput = open(problem + '-' + s_input + '-' + s_id + '.out','w')
	foutput.writelines(result)
	foutput.close()

##########################################################################################################################

def StrToNumList(s):
	#return [int(x) for x in re.findall('[0-9\-]+',s)]
	return [int(x) for x in s[:-1].split()]

##########################################################################################################################

def StrToNum(s):
	return int(s[:-1])

##########################################################################################################################

def innerProd(x,y):
	return sum([i*j for i,j in zip(x,y)])

##########################################################################################################################

def storeCredit(L):
	credit, items = StrToNum(L[0]), StrToNumList(L[2])
	d = {}
	for item, price in enumerate(items,1):
		if price in d:
			return "%s %s" %(d[price], item)
		else:
			d[credit-price] = item

##########################################################################################################################

def reverseWords(s):
	return ' '.join(reversed(s.split()))

##########################################################################################################################

def minScalarProd(L):
	v1, v2 = StrToNumList(L[0]), StrToNumList(L[1])
	return innerProd(sorted(v1), reversed(sorted(v2)))

##########################################################################################################################

def validate_customer(flav, customer):
	nLikes, pref = customer[0], customer[1:]
	malted_flav_index = "IMPOSSIBLE"
	for i in range(nLikes):
		if pref[2*i+1] == flav[pref[2*i]-1]:
			return "Satisfied"
		elif pref[2*i+1] == 1 and flav[pref[2*i]-1]==0:
			malted_flav_index = pref[2*i]-1
	return malted_flav_index

##########################################################################################################################

def validate_preference(f, c):
	for cust in c:
		r = validate_customer(f, cust)
		if r == "Satisfied":
			pass
		elif r == "IMPOSSIBLE":
			return r
		else:
			f[r] = 1
			c.remove(cust)
			return validate_preference(f,c)
	return ' '.join([str(x) for x in  f])

##########################################################################################################################

def milkShake(L):
	flavours = [0]*StrToNum(L[0])
	customers = [StrToNumList(c) for c in L[2:] ]
	return validate_preference(flavours, customers)

##########################################################################################################################

def pad(lt, rt):
    if rt[:1] == lt[-1:]:
        lt += ' '
    return lt + rt

##########################################################################################################################

def t9(s):
	s = s[:-1]
	if not s:
		return ''
	keymap = " ,,abc,def,ghi,jkl,mno,pqrs,tuv,wxyz".split(',')
	t9map = {char:str(key)*repeat for key,label in enumerate(keymap) for repeat,char in enumerate(label,1)}
	return reduce(pad, map(t9map.get, s))

##########################################################################################################################

def recur_multi(m,n):
	if n == 1:
		#print m, 'n=1 so returned'
		return m
	else:
		if n % 2 == 0:
			#print m, n, 'n is even so disected into two of:', n/2
			return np.dot(recur_multi(m,n/2),recur_multi(m,n/2))%1000
		else:
			#print m, n, 'n is further result is:', (np.mat(m)*np.mat(recur_multi(m,n-1)))%1000
			return np.dot(m,recur_multi(m,n-1))

##########################################################################################################################

def matrix_mult(A, B):
	C = [[0, 0], [0, 0]]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % 1000
	return C

##########################################################################################################################

def fast_exponentiation(A, n):
	if n == 1:
		return A
	else:
		if n % 2 == 0:
			A1 = fast_exponentiation(A, n/2)
			return matrix_mult(A1, A1)
		else:
			return matrix_mult(A, fast_exponentiation(A, n - 1))

##########################################################################################################################

def numbers_power(s):
	n = StrToNum(s)
	#return (recur_multi(np.mat( [[3, 5], [1, 3]]),n)[0,0]*2 + 999)%1000
	A = [[3, 5], [1, 3]]
	A_n = fast_exponentiation(A, n)
	return (2 * A_n[0][0] + 999) % 1000

##########################################################################################################################

def alien_lang(s,d):
	test = reduce(lambda x, y: x.strip() + ' ' + y.strip(), [item for item in d])
	s = s.strip().replace(')',']')
	s = s.replace('(','[')
	return len(re.findall(s,test))

##########################################################################################################################

def googlerese(s):
	s = s.strip()
	d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
	return reduce(lambda x, y: x + y, map(d.get, s))

##########################################################################################################################

def dance_scores(l):
	l = StrToNumList(l)
	n = l.pop(0)
	s = l.pop(0)
	p = l.pop(0)
	if p == 0:
		return len(l)
	elif p == 1:
		return len(filter(lambda x: x > 0, l))
	else:
		return len(filter(lambda x: x > 3*(p-1),l)) + min(s,len(filter(lambda x: x == (3*p-3) or x == (3*p-4), l)))

##########################################################################################################################

def permute(s,a,b):
	s = str(s)
	l = []
	l = set([s[i:]+s[:i] for i in range(len(s)) if int(s) <= int(s[i:]+s[:i]) <= b ])
	ans = 0
	if len(l) > 1:
		#ans = math.factorial(len(l))/(math.factorial(len(l)-2)*2)
		ans = len(l) -1
	return ans, l

##########################################################################################################################

def rec_nums(l):
	a, b = StrToNumList(l)
	d = {}
	d = {str(i):i for i in range(a, b + 1)}
	ans = 0
	while d:
		item, l = permute(d.iterkeys().next(),a,b)
		[d.pop(key,None) for key in l]
		ans += item
	return ans

##########################################################################################################################

def rec_nums1(l):
	a, b = StrToNumList(l)
	ans = 0
	for i in range(a,b+1):
		item, l = permute(i,a,b)
		ans += item
	return ans

##########################################################################################################################
