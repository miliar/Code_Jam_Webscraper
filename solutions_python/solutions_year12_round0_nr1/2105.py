import sys

f = open('a-small-attempt1.in')
s = open("salida.txt","w")
x = f.readline()
n = int(x)

alfabeto = "abcdefghijklmnopqrstuvwxyz"
cambios  = "yhesocvxduiglbkrztnwjpfmaq"
frases = []
for i in range(n):
	frases.append(f.readline().split())

i = 0
while i < n:
	nueva_frase = []
	frase = frases[i]
	for x in frase:
		palabra = ""
		for y in x:
			posicion = alfabeto.index(y)
			palabra += cambios[posicion]
		nueva_frase.append(palabra)
	s.write("Case #" + str(i+1) + ": " + ' '.join([ c for c in nueva_frase]) + "\n")
	i += 1