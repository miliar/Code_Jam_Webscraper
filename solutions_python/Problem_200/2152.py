

def isTidy(listNumber):
	for i in range(len(listNumber)-1):
		if listNumber[i] > listNumber[i+1]:
			return i+1
	return -1

def borrarCerosIniciales(lista):
	res = []
	primeros = True
	for a in lista:
		if a != 0 or not primeros:
			res += [a]
			primeros = False
	return res

def apply9(lista,frstProblem):

	size = len(lista)

	for i in range(size):
		if i >= frstProblem:
			lista[i] = 9

	return lista 

def largestTidy(number):

	lista = [ int(x) for x in list(str(number))]

	frstProblem = isTidy(lista)

	while (frstProblem != -1):
		lista[frstProblem-1] -= 1
		
		lista = apply9(lista,frstProblem)

		frstProblem = isTidy(lista)

	lista =	borrarCerosIniciales(lista)

	lista = map(str, lista) 

	return ''.join(lista)

with open('./B-large.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

content = content[1:]
print content
i = 0
for a in content:
	i += 1
	print "Case #" + str(i) + ": " + str(largestTidy(int(a)))