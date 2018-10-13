 
 
def calculaViradas():
	entrada = recebeEntrada()
	if entrada == "":
		return False
	T, sMatriz, kVetor = leEntrada(entrada)
	assert ((T == len(sMatriz) and (T == len(kVetor))))
	saida = ""
	for i, k in enumerate(kVetor):
		linha = sMatriz[i]
		val = resolveCaso(linha, k)
		saida += "Case #" + str(i+1) + ": " + val + "\n"
	saida = saida[:-1]
	print(saida)
	return saida
	
def recebeEntrada():
	texto = []
	try:
		texto = [input(), ]
		if texto == "":
			return ""
		T = int(texto[0])
		while T > 0:
			texto.append(input())
			T -= 1
	except EOFError:
		pass
	return "\n".join(texto)
	
def leEntrada(entrada):
	linhas = entrada.split("\n")
	T = int(linhas[0])
	matriz = []
	vetor = []
	for linha in linhas[1:]:
		trechos = linha.split(' ')
		valores = []
		for caractere in trechos[0]:
			if caractere == "-":
				valores.append(False)
			elif caractere == "+":
				valores.append(True)
			else:
				raise Exception()
		matriz.append(valores)
		vetor.append(int(trechos[1]))
	return T, matriz, vetor
		
def resolveCaso(linha, k):
	tamanho = len(linha)
	num = 0
	for i, val in enumerate(linha):
		if val:
			pass
		elif not val:
			if k > tamanho - i:
				num = "IMPOSSIBLE"
				break
			else:
				num += 1
				for j in range(k):
					linha[i+j] = not linha[i+j]
		else:
			raise Exception()
	return str(num)
	
if __name__ == "__main__":
	while calculaViradas():
		pass
