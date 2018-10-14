def hacer(lista, k):
	if lista[k]<lista[k+1]:
		for j in range(k+1):
			lista[j]=9
		lista[k+1]-=1
	return(lista)


problemas = int(input())
for problema in range(problemas):
	nivel = int(input())
	lista = [int(k) for k in str(nivel)[::-1]]
	for k in range(len(lista)-1):
		lista = hacer(lista,k)
	print("Case #"+str(problema+1)+": "+str(int("".join(str(k) for k in reversed(lista)))))