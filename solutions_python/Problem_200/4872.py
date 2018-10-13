prueba = open('B-small-attempt0.in', 'r')
new_tex = []
new_tex1 = []
res = []
file = open('Respuestas.txt', 'w')


for linea in prueba:
	if linea[-1] == '\n':
		linea = linea[:-1]
	new_tex.append(linea)


for i in new_tex:
	i = int(i)
	new_tex1.append(i)
#print new_tex1 

#programa
num_casos = new_tex1[0]
new_tex1.pop(0)
caso = 1

for i in new_tex1:
	digitos = [int (x) for x in str(i)]
	orden_dig = digitos[:]
	orden_dig.sort()

	while orden_dig != digitos:
		i -= 1
		digitos = [int (j) for j in str(i)]
		orden_dig = digitos[:]
		orden_dig.sort()
	i1 = "Case #" + str(caso) + ": " + str(i)
	caso += 1
	res.append(i1)

for w in res:
	file.write(w)
	file.write('\n')






