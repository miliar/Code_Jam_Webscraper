data = open('welcome.txt', 'r').read().split('\n')

N = int(data.pop(0))

global totalFound
totalFound = 0

def differentWays(entrada, buscada, start, indice):
	global totalFound
	
	if indice == 18:
		for i in range(start, len(entrada)):
			if entrada[i] == buscada[indice]:
				totalFound += 1
		return
	
	for i in range(start, len(entrada)):
		if entrada[i] == buscada[indice]:
			differentWays(entrada, buscada, i+1, indice+1)

for i in range(N):
	line = data.pop(0)
	differentWays(line, 'welcome to code jam', 0, 0)
	print 'Case #' + str(i+1) + ': ' + str(totalFound).zfill(4)
	totalFound = 0
