import itertools
from copy import copy

def keystrokes(estado, total, borrar):
	estado = list(copy(estado))
	if borrar == len(estado)+1:
		return 1+total+1 #Los dos enter y el total
	else:
		# for i in range(borrar):
			# estado.pop()
		restantes = len(estado)-borrar
		tot = borrar+total-restantes+1
		if not borrar == 0:
			estado = estado[:-borrar]
		if 0 in estado: #Si hay uno malo
			tot += total+1 # Lo vuelvo a repetir
		return tot

entrada = open('small.in', 'r')
salida  = open('small.out', 'w')

casos = int(entrada.readline())

for i in xrange(casos):
	tipeados, totales = map(int, entrada.readline().split())
	probabilidades = map(float, entrada.readline().split())

	productos = list(itertools.product([1, 0], repeat=tipeados))
	total_prob = [1] * len(productos)
	for j, p in enumerate(productos):
		for index, probabilidad in enumerate(probabilidades):
			if p[index]:
				total_prob[j] *= probabilidad
			else:
				total_prob[j] *= (1-probabilidad)

	dict_key = {}

	for j in range(tipeados+2):
		dict_key[j] = []
		for w in productos:
			dict_key[j].append(keystrokes(w, totales, j))

	totals = []
	for key in dict_key:
		totals.append(sum([x*y for x, y in zip(total_prob, dict_key[key])]))

	salida.write('Case #%d: %0.6f\n' % (i+1, min(totals)))

