
import sys
import time
import operator
import math
import re


timeit = 1
debugv = 0
startTime = 0

outFile = open('output.txt', 'w')
inFile = sys.stdin
inFile = open('C-test.in', 'r')
inFile = open('C:/Users/quentin/Downloads/C-small-attempt1.in', 'r')
#inFile = open('C:/Users/quentin/Downloads/C-large.in', 'r')

def main():
	T = int(inFile.readline())
	startTime = time.clock()
	for case in range(1,T+1):
		out("Case #{}: ".format(case))
		doCase(case)
		out("\n")

		



def out(m):
	outFile.write(m)
	sys.stdout.write(m)

dic = {
	'1':{'1':'1', 'i':'i', 'j':'j', 'k':'k'},
	'i':{'1':'i', 'i':'1', 'j':'k', 'k':'j'},
	'j':{'1':'j', 'i':'k', 'j':'1', 'k':'i'},
	'k':{'1':'k', 'i':'j', 'j':'i', 'k':'1'},
}
sig = {
	'1':{'1':1, 'i':1, 'j':1, 'k':1},
	'i':{'1':1, 'i':-1, 'j':1, 'k':-1},
	'j':{'1':1, 'i':-1, 'j':-1, 'k':1},
	'k':{'1':1, 'i':1, 'j':-1, 'k':-1},
}

def mult(a,b, s=1):
	return dic[a][b], sig[a][b]*s



def doCase(case):
	L, X = [int(x) for x in inFile.readline().split()]
	st = inFile.readline()[0:-1]
	S = ""
	'''for c in st:
					t, s = mult(t, c, s)
				if s == -1 and X%2 != 0:
					out("NO")
					return'''

	for i in range(X):
		S+=st

	I = '1', 1
	J = set()
	K = set()
	for st in S:

		NJ = set()
		for j in J:
			NJ.add(mult(j[0], st, j[1]))
		J = NJ

		NK = set()
		for k in K:
			NK.add(mult(k[0], st, k[1]))
		K = NK

		if ('j', 1) in J:
			u = '1', 1
			K.add(u)

		I = mult(I[0], st, I[1])
		if I == ('i', 1):
			u = '1', 1
			J.add(u)
	if ('k', 1) in K:
		out('YES')
	else:
		out("NO")
'''	t ='1'
	s = 1
	idx = 0
	for st in S:
		idx += 1
		t, s = mult(t, st, s)
		if t == 'i' and s == 1:
			#print("idx1:"+str(idx))
			t2 = '1'
			s2 = 1
			idx2 = len(S)
			for st2 in S[:len(S) - idx-1:-1]:
				idx2 -= 1
				t2, s2 = mult(st2, t2, s2)
				if t2 == 'k' and s == 1:
					#print("idx2:"+str(idx2))
					#print("remain:"+S[idx:idx2])
					t3 = '1'
					s3 = 1
					for st3 in S[idx:idx2]:
						t3, s3 = mult(t3, st3, s3)
					if t3 == 'j' and s == 1:
						out("YES")
						return
'''

	#print(S)


	#out(str(count))






def debugln(m):
	debug(m)
	debug('\n')

def debug(m):
	if debugv:
		sys.stdout.write(str(m))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if re.search('d', sys.argv[1]):
			debugv = 1
		if re.search('i', sys.argv[1]):
			inFile = sys.stdin

	main()
	if timeit:
		sys.stderr.write("Completed in {} seconds.\n".format(time.clock() - startTime)) 