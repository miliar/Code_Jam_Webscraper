
'''
1 = 1
2 = i
3 = j
4 = k
'''
def mult(a,b):
	sig = 1 if a*b>0 else -1
	a = abs(a)
	b = abs(b)
	if a==1:
		return b * sig
	if b==1:
		return a * sig


	if a==2:
		if b==2:
			return -1 * sig
		if b==3:
			return  4 * sig
		if b==4:
			return -3 * sig

	if a==3:
		if b==2:
			return -4 * sig
		if b==3:
			return -1 * sig
		if b==4:
			return  2 * sig

	if a==4:
		if b==2:
			return  3 * sig
		if b==3:
			return -2 * sig
		if b==4:
			return -1 * sig

def change(c):
	if c=='i':
		return 2
	if c=='j':
		return 3
	if c=='k':
		return 4



def getTotal(cad):
	
	i = 1
	for b in cad:
		i = mult(i,b)
	print 'Toda Cadena ', i
	return i

def getRes(cad, ind):
	cad = map(change,cad)
	total = getTotal(cad)
	if total != -1:
		return 'Case #%d: NO\n'% ind
	res = 0
	#print 'Res = ', cad

	l = len(cad)

	#Find I
	prevI = 1
	i = 0
	iFound = False
	while i<l:
		prevI = mult(prevI, cad[i])
		if prevI==2:
			#print 'i Found, from 0 to ',i
			print 'I Found!'
			iFound = True
			break
		i+=1

	if not iFound:
		return 'Case #%d: NO\n'% ind
	#find K
	prevK = 1
	k = l-1
	kFound = False
	while k>=0:
		prevK = mult(cad[k],prevK)
		k-=1
		if prevK==4:
			print 'K found!'
			kFound = True
			break

	if not kFound:
		return 'Case #%d: NO\n'% ind
	if i<k:
		return 'Case #%d: YES\n'% ind

	return 'Case #%d: NO\n'% ind

inp = open('small.in','r')

f = open('small.out','w')

T = int(inp.readline())

for x in range(T):
	i = x+1
	l,x = map(int,inp.readline().split(' '))
	cad = inp.readline().strip()
	f.write( getRes(cad*x, i) )

inp.close()
f.close()


