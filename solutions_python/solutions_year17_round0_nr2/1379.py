 
def númeroArrumado():
	texto = lêEntrada()
	while texto != "":
		T, nMatriz = processaEntrada(texto)
		calculaResultado(T, nMatriz)
		texto = lêEntrada()

def lêEntrada():
	try:
		texto = input()
		num = int(texto)
		texto += "\n"
		for i in range(num):
			texto += input() + "\n"
		texto = texto[:-1]
		return texto
	except EOFError:
		return ""

def processaEntrada(texto):
	linhas = texto.split("\n")
	T = int(linhas[0])
	matriz = []
	for linha in linhas[1:]:
		vet = []
		for caractere in linha:
			vet.append(int(caractere))
		matriz.append(vet)
	assert(len(matriz) == T)
	return T, matriz
	
def calculaResultado(T, nMatriz):
	resultado = ""
	for i, numeros in enumerate(nMatriz):
		numerosAlterados = numeros
		desordem = buscaDesordem(numerosAlterados)
		while desordem:
			numerosAlterados  = arrumaNúmero(desordem, numerosAlterados)
			desordem = buscaDesordem(numerosAlterados)
		imprimeCasosDeTeste(numerosAlterados, i)
		
def buscaDesordem(vet):
	for i in range(len(vet) - 1):
		if vet[i] > vet[i + 1]:
			return i + 1
	return False
	
def arrumaNúmero(pos, vet):
	vet[pos-1] -= 1
	for i in range(len(vet) - pos):
		vet[pos + i] = 9
	return vet
	
def imprimeCasosDeTeste(vet, i):
	numero = int("".join([str(j) for j in vet]))
	print("Case #" + str(i+1) + ": " + str(numero))
	
if __name__ == "__main__":
	númeroArrumado()
