import sys

f = open('in.txt', 'r')
f1= open('out.txt','w')

line = f.readline()

def resi(niz):
	rez = 0
	palacinke, spatula = niz.split(' ')
	palacinke = list(palacinke)
	for i in range(len(palacinke)- int(spatula)+1):
		if palacinke[i] == '-':
			if palacinke[i] == '-':
				palacinke[i] = '+'
			else:
				palacinke[i] = '-'
			rez += 1
			for s in range(int(spatula)-1):
				if palacinke[i+s+1] == '-':
					palacinke[i+s+1] = '+'
				else:
					palacinke[i+s+1] = '-'
	for i in range(len(palacinke)- int(spatula), len(palacinke)):
		if palacinke[i] == '-':
			return 'IMPOSSIBLE'
	return str(rez)

for a in range(int(line)):
	line = f.readline().strip()
	f1.write('Case #'+str(a+1)+': ' + resi(line)+'\n')
	
