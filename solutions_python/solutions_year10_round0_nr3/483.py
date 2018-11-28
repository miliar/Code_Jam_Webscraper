import sys
import psyco

def quitar(cola):
    return cola.remove(cola[0])

def poner(cola, elto):
	cola.append(elto)

def consultar(cola):
	return cola[0]

def solve(R, K, cola):
	res = 0
	colaAUX = []
	personas = 0
	N = 0
	while (R > 0):
		R -= 1
		colaAUX = []
		personas = 0
		N = len(cola)
		while (cola!=[] and N > 0):
			N -= 1
			if (K - personas >= int(consultar(cola))):
				personas += int(consultar(cola))
				res += int(consultar(cola))
				poner(cola, consultar(cola))
				quitar(cola)
			else:
				break
	
	return res

def main():
	file = open(sys.argv[1])
	
	j = int(file.readline()) + 1
    
	cola = []
	R = 0
	K = 0
	lenght = 0
    
	for i in range(1, j):
		R, K, lenght = map(int, file.readline().split())
		cola = map(int, file.readline().split())
		res = solve(R, K, cola)
		print "Case #%i: %i" % (i, res)

	file.close()

if __name__ == "__main__":
	psyco.full()
	main()
	
