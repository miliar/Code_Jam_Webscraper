

def apply(i, k, palabra):
	for j in range(k):
		switch(palabra,i+j)
	return palabra

def switch(palabra, i):

		if palabra[i] == '+':
			palabra[i] = '-'
		else:
			palabra[i] = '+'

def allUp(palabra):
	for a in palabra:
		if a != "+":
			return False
	return True

def pancakeUp(palabra,k):

	if k > len(palabra):
		print "IMPOSSIBLE"
		return

	lista = list(palabra)

	moves = 0

	for i in range(len(lista)-k+1):
		if lista[i] == '-':
			lista = apply(i,k,lista)
			moves +=1
	
	if allUp(lista):
		return moves
	else:
		return "IMPOSSIBLE"

with open('./A-large.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

content = content[1:]
i = 0
for a in content:
	i += 1
	aux = a.split()
	res = pancakeUp(aux[0],int(aux[1]))
	print "Case #" + str(i) + ": " + str(res)
