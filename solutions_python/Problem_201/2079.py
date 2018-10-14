'''
A certain bathroom has N + 2 stalls in a single row;
 the stalls on the left and right ends are permanently occupied by the bathroom guards.
  The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible.
To avoid confusion, they follow deterministic rules: For each empty stall S,
they compute two values LS and RS,
each of which is the number of empty stalls between S and the closest occupied stall to the left or right,
respectively. Then they consider the set of stalls with the farthest closest neighbor, 
that is, those S for which min(LS, RS) is maximal. If there is only one such stall,
they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal.
If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives.
 Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?

Solving this problem

This problem has 2 Small datasets and 1 Large dataset.
You must solve the first Small dataset before you can attempt the second Small dataset.
You will be able to retry either of the Small datasets (with a time penalty).
You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.

Input

The first line of the input gives the number of test cases, T. T lines follow.
Each line describes a test case with two integers N and K, as described above.

Output

For each test case, output one line containing Case #x: y z,
where x is the test case number (starting from 1), y is max(LS, RS),
and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.


o........o
o...o....o
o...o.o..o
o.o.o.o..o
ooo.o.o..o



 	
Output 
 
5
4 2
5 2
6 2
1000 1000
1000 1

Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499


4 2

o....o
o.o..o
o.oo.o


Case #1: 1 0


'''

import sys
import math

def stallsProblem(n, k):

	ocupados = [0,n+1]

	stalls = [(-1,-1)]+[(x,n-x-1) for x in range(n)]+[(-1,-1)]

	n = n+2

	for i in range(k):

		# calculo min(LS,RS)

		maxmin = min(stalls[0])

		for tupla in stalls:
			if min(tupla) > maxmin:	
				maxmin = min(tupla)

		# Calculo quienes son

		maxmins = []

		for i in range(len(stalls)):
			if min(stalls[i]) == maxmin:
				maxmins.append(i)

		# calculo max(LS,RS)

		maxmax = max(stalls[maxmins[0]])

		for i in maxmins:
			if max(stalls[i]) > maxmax:
				maxmax = max(stalls[i])

		# me quedo con el primero de esos (El mas a la izquierda)

		res_i = maxmins[0]

		for i in maxmins:
			if max(stalls[i]) == maxmax:
				res_i = i
				break

		res = (max(stalls[res_i]),min(stalls[res_i]))

		ocupados, anterior, posterior = insertarOrdenado(ocupados,res_i)

		stalls[res_i] = (-1,-1)

		stalls = actualizar(stalls,anterior,res_i,posterior)

	return res

def actualizar(lista,anterior,nuevo,posterior):

	if anterior != -1:
		n = len(lista[anterior+1:nuevo])

		for i in range(n):
			lista[anterior+i+1] = (i,n-i-1)

	if posterior != -1:
		n = len(lista[nuevo+1:posterior])

		for i in range(n):
			lista[nuevo+i+1] = (i,n-i-1)

	return lista

def insertarOrdenado(lista, elem):

	n = len(lista)

	pos = n

	for i in range(len(lista)):
		if lista[i] > elem:
			pos = i
			break

	lista = lista[:pos] + [elem] + lista[pos:]

	if pos == 0:
		anterior = -1
	else:
		anterior = lista[pos-1]

	if pos == n:
		posterior = -1
	else:
		posterior = lista[pos+1]

	return lista, anterior, posterior


def main(argv):

	with open(argv[0], 'r') as f:
	    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [ x.strip() for x in content ]

	content = content[1:]

	with open('./output.txt', 'w') as f:
		i = 0
		for a in content:
			aux = a.split()
			i += 1
			res = stallsProblem(int(aux[0]),int(aux[1]))
			f.write("Case #" + str(i) + ": " + str(res[0]) + " " + str(res[1]) + '\n')
 
if __name__ == "__main__":
    main(sys.argv[1:])

