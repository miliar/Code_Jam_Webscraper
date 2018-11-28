import math

fin = open('C-large.in', 'r')
fout = open('out.txt', 'w')

T = int(fin.readline())

for t in xrange(T):
	L, X = fin.readline().split()
	P = fin.readline()
	a = 1
	soma = ord('i')+ord('j')+ord('k')
	ok = ord('i')
	res = "NO"
	
	for x in xrange(min(int(X),13)):
		for l in xrange(int(L)):
			b = ord(P[l]);
			inv = a/abs(a);
			a = abs(a);
			if a==1: a=inv*a*b
			elif a==b: a=-1*inv
			elif a-b==2: a=inv*(soma-a-b)
			elif a-b==1: a=-inv*(soma-a-b)
			elif a-b==-1: a=inv*(soma-a-b)
			elif a-b==-2: a=-inv*(soma-a-b)
			if a==ok:
				if ok<ord('k'):
					ok+=1
					a = 1
				elif l==int(L)-1 and (int(X)-x-1)%4==0: 
					res="YES"
					break
		if res=="YES": break
				
	fout.write("Case #%d: %s\n" %(t+1, res))

fin.close()
fout.close()