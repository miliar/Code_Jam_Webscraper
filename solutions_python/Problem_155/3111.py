
def calculaAmigos(listaDeTimidez):
	amigos = 0
	especConq = 0
	for nivel in range(len(listaDeTimidez)):
		if nivel > amigos + especConq:
			amigos += nivel - (amigos + especConq)
		especConq += listaDeTimidez[nivel]
	return amigos

def imprimeResultado(numDoCaso, res):
	print("Case #%d: %d" % (numDoCaso+1, res))


if __name__ == "__main__":
	numCasos = int(input())
	for i in range(numCasos):
		nums = input()
		div = nums.split(" ")
		timidezMax = int(div[0])
		listaDeTimidez = [int(elem) for elem in div[1]]
		resultado = calculaAmigos(listaDeTimidez)
		imprimeResultado(i, resultado)
		numCasos = numCasos - 1