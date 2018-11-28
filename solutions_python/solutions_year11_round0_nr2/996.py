def borrar(car, cants, tabla):
	i = 0
	while i < len(cants):
		if cants[i] > 0:
			if tabla[car][i] == 1:
				return 1
		i = i + 1
	return 0

def borrarcants(cants):
	i = 0
	while i < len(cants):
		cants[i] = 0
		i = i + 1
		
def salida(cad):
	s = "["
	i = 1
	if len(cad) > 0:
		s += cad[0]
	while i < len(cad):
		s += ", "
		s += cad[i]
		i = i + 1
	s += "]"
	return s

fin = open('./Descargas/B-large.in','r')
fout = open('./B.out','w')

indices = dict()
indices["A"] = 0
indices["B"] = 1
indices["C"] = 2
indices["D"] = 3
indices["E"] = 4
indices["F"] = 5
indices["G"] = 6
indices["H"] = 7
indices["I"] = 8
indices["J"] = 9
indices["K"] = 10
indices["L"] = 11
indices["M"] = 12
indices["N"] = 13
indices["O"] = 14
indices["P"] = 15
indices["Q"] = 16
indices["R"] = 17
indices["S"] = 18
indices["T"] = 19
indices["U"] = 20
indices["V"] = 21
indices["W"] = 22
indices["X"] = 23
indices["Y"] = 24
indices["Z"] = 25

t = int(fin.readline())
i0 = 0
while i0 < t:
	tablacombinacion = list()
	tablaopuestos = list()
	fila1 = []
	fila2 = []
	cants = []
	for l in indices.keys():
		fila1.append("NO")
		fila2.append(0)
	for l in indices.keys():
		copia1 = fila1[:]
		copia2 = fila2[:]
		tablacombinacion.append(copia1)
		tablaopuestos.append(copia2)
		cants.append(0)

	ps = fin.readline().split()
	c = int(ps[0])
	i1 = 1
	while i1 < c + 1:
		cad = ps[i1]
		elem1 = indices[cad[0]]
		elem2 = indices[cad[1]]
		elemres = cad[2]
		tablacombinacion[elem1][elem2] = elemres
		tablacombinacion[elem2][elem1] = elemres
		i1 = i1 + 1
	d = int(ps[i1])
	i1 = i1 + 1
	while i1 < d + 1 + c + 1:
		cad = ps[i1]
		elem1 = indices[cad[0]]
		elem2 = indices[cad[1]]
		tablaopuestos[elem1][elem2] = 1
		tablaopuestos[elem2][elem1] = 1
		i1 = i1 + 1
	n = int(ps[i1])
	simb = ps[i1 + 1]
	i2 = 0
	cad = str()
	while i2 < n:
		caracter = simb[i2]
		if len(cad) == 0:
			cad += (caracter)
			cants[indices[caracter]] = cants[indices[caracter]] + 1
		else:
			anterior = cad[len(cad) - 1]
			if tablacombinacion[indices[caracter]][indices[anterior]] != "NO":
				cad = cad[:len(cad) - 1]
				cad += (tablacombinacion[indices[caracter]][indices[anterior]])
				cants[indices[tablacombinacion[indices[caracter]][indices[anterior]]]] = cants[indices[tablacombinacion[indices[caracter]][indices[anterior]]]] + 1
				cants[indices[anterior]] = cants[indices[anterior]] - 1
			else:
				if(borrar(indices[caracter], cants, tablaopuestos) == 1):
					cad = str()
					borrarcants(cants)
				else:
					cad += (caracter)
					cants[indices[caracter]] = cants[indices[caracter]] + 1
		i2 = i2 + 1
	fout.write("Case #" + str(i0 + 1) + ": " + salida(cad) + "\n")	
	i0 = i0 + 1
