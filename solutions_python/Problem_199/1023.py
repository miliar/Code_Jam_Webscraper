archivo = open('A-large.in')

archivo.readline()

lista=[]

for linea in archivo.readlines ():
	lista.append(linea.split())
	
def funcion (S, K):
	veces=0
	string=[]
	for item in S:
		string.append(item)
	x=0
	while x <= len (string)-K:
		if string[x]=='-':
			veces+=1
			string[x]='+'			
			for i in xrange (1,K):
				if string[x+i]=='-':
					string[x+i]='+'
				else:
					string[x+i]='-'
		x+=1
	contador=0
	for a in xrange ( len (S)):
		if string[a]=='+':
			contador+=1
	if contador==len(S):
		return veces
	else:
		return 'IMPOSSIBLE'
		
for i, item in enumerate(lista):
	print "Case #{}: {}".format(i+1, funcion (item[0], int(item[1])))
	
	
	

