# -1 = 2
# -i = l
# -j = m
# -k = n

def multi(a,b):
	if a == '1':
		return b

	elif a == 'i':
		if b == 'i':
			return '2'
		elif b == 'j':
			return 'k'
		else:
			return 'm'
	
	elif a == 'j':
		if b == 'i':
			return 'n'
		elif b == 'j':
			return '2'
		else:
			return 'i'
	
	elif a == 'k':
		if b == 'i':
			return 'j'
		elif b == 'j':
			return 'l'
		else:
			return '2'
	
	elif a == '2':
		if b == 'i':
			return 'l'
		elif b == 'j':
			return 'm'
		else:
			return 'n'
	
	elif a == 'l':
		if b == 'i':
			return '1'
		elif b == 'j':
			return 'n'
		else:
			return 'j'
	
	elif a == 'm':
		if b == 'i':
			return 'k'
		elif b == 'j':
			return '1'
		else:
			return 'l'
	
	else:
		if b == 'i':
			return 'm'
		elif b == 'j':
			return 'i'
		else:
			return '1'

def multi_reste(a):
	res = '1'
	for char in a:
		res = multi(res,char)
	return res

def est_reductible(a):
	res = '1'
	iok = False
	jok = False
	longueur = len(a)
	for i in range(longueur):
		res = multi(res,a[i])
		if not iok and res == 'i':
			res = '1'
			iok = True
		elif iok and not jok and res == 'j':
			res = '1'
			jok = True
		elif iok and jok :
			if 'k' == multi_reste(a[i:longueur]):
				return 'YES'
			else:
				return 'NO'
	return 'NO'

def chaine(a,b):
	res = ''
	for i in range(int(b)):
		res += a
	return res

def solution_jam2():
	source = open("D:/Download/test.txt","r")
	output = open("D:/Download/jam2small.txt","w")
	liste = source.readline()
	liste = liste.split('\n')
	for i in range(int(liste[0])):
		liste1 = source.readline()
		liste1 = liste1.split()
		liste2 = source.readline()
		liste2 = liste2.split()
		mot = chaine(liste2[0],liste1[1])
		output.write('Case #'+str(i+1)+': '+ est_reductible(mot)+'\n')
	output.close()
	source.close()

solution_jam2()


	