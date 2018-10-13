

entrada = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
saida = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"

dic = {}
for i in range(len(entrada)):
	dic[entrada[i]] = saida[i]

dic['z']= 'q'
dic['q']= 'z' 

num_entradas = int(raw_input())

entradas = [raw_input() for x in range(num_entradas)]

for n,j in enumerate(entradas):
	
	b = ""
	for i in range(len(j)):
		
		if j[i] in dic:
			b+= dic[j[i]]
		else:
			b+=j[i]
	print"Case #%i: %s"%(n+1, b)
