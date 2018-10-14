import re, sys

fin = open(sys.argv[1], "r")
entrada = fin.readline().split()
L = int(entrada[0]);
D = int(entrada[1]);
N = int(entrada[2]);
diccionario = [];

for i in range(0,D):
	entrada = fin.readline()
	diccionario.append(entrada)
	
for i in range(0,N):
	entrada = fin.readline()
	entrada = re.sub("\(", "[", entrada)
	entrada = re.sub("\)", "]", entrada)
	word = re.compile(entrada)
	contador = 0
	for j in diccionario:
		if word.match(j):
			contador += 1
	salida = "Case #"+str(i+1)+": "+str(contador)
	print salida