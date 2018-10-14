def conta_frases(frase, lista, indice):
	nLetra = frase.count(lista[0], indice)
	
	if nLetra == 0:
		return nLetra
	
	elif len(lista) == 1:
		return nLetra
	
	elif len(lista) > 1:
		pos = 0
		ind_int = indice
		for c in range(nLetra):
			ind_int = frase.find(lista[0], ind_int) + 1
			pos += conta_frases(frase, lista[1:], ind_int)
		return pos
arquivo = open("C2.txt", "w")
FRASE_COMPARAR = "welcome to code jam"

N_testes = input()

lista_letras = []
for letra in FRASE_COMPARAR:
	lista_letras.append(letra)

for N in range(N_testes):
	frase_test = raw_input()
	n_posib = conta_frases(frase_test, lista_letras, 0)
	
	arquivo.write("Case #%d: %0.4d\n" % ((N +1), n_posib))
arquivo.close()
	
