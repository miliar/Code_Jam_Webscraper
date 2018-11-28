def listaPossibilidades(ent, parametro):
	listaPos = []
	i = 0
	while i < len(ent):
		if ent[i] == "(":
			local = ent.find(")", i + 1)
			listaPos.append(ent[i+1: local])
			i = local + 1
		else:
			listaPos.append(ent[i])
			i += 1
			
	return listaPos

def booElemlista(elementos, listapos):
	for i in range(len(elementos)):
		if not elementos[i] in listapos[i]:
			return False
	return True
		
def quantpos(listapos, lisatest):
	count = 0
	for elemento in lisatest:
		if booElemlista(elemento, listapos):
			
			count += 1
	return count
	
parametrosInteiros = raw_input().split()

arquivo = open("A-large.txt", "w")

L, D, N = int(parametrosInteiros[0]), int(parametrosInteiros[1]), int(parametrosInteiros[2])

lista_test = []

for i in range(D):
	lista_test.append(raw_input())

for num in range(N):
	casoT = raw_input()
	
	possibilit = listaPossibilidades(casoT, L)
	arquivo.write("Case #%d: %d\n" % ((num + 1), quantpos(possibilit, lista_test)))

arquivo.close()
