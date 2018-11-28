
from sys import argv

fname = argv[1]
f = open(fname, 'r')

content = f.read().split('\n')


ncases = int(content[0])

for ncase in range(1, 1 + ncases):
	
	shymax, shychain = content[ncase].split(' ')
	
	shylist = []
	for i in range(len(shychain)):
		shylist.extend([int(shychain[i])])
	#print(shylist)	
	
	nactiv = 0
	nfriends = 0
	for i in range(len(shylist)):
		if shylist[i] > 0:
			if (nactiv >= i):
				nactiv += shylist[i]
			else:
				ndiff = (i - nactiv)
				nactiv += ndiff
				nfriends += ndiff
				nactiv += shylist[i]
		#print(i, nactiv, nfriends)
	print('Case #%d: %d' % (ncase, nfriends))