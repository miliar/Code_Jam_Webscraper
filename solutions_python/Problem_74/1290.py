import sys

archivo = open(sys.argv[1],'r')
archsale = open(sys.argv[2],'w')

cantTests = int(archivo.readline())

for i in range(1,cantTests+1) :
	ordenes = archivo.readline().split(" ")
	cantOrdenes = int(ordenes[0])
	BPos = 1
	OPos = 1
	Bpasosafavor = 0
	Opasosafavor = 0
	pasosTotales = 0
	j = 1
	while (j < 2*cantOrdenes) :
		if (ordenes[j]=="O") :
			pasosahacer = abs(OPos - int(ordenes[j+1]))
			if (pasosahacer > Opasosafavor) :
				pasosTotales += pasosahacer - Opasosafavor + 1
				Bpasosafavor += pasosahacer - Opasosafavor + 1
				Opasosafavor = 0
			else :
				pasosTotales += 1
				Opasosafavor = 0
				Bpasosafavor += 1

			OPos = int(ordenes[j+1])

		else:
			pasosahacer = abs(BPos - int(ordenes[j+1]))
			if (pasosahacer > Bpasosafavor) :
				pasosTotales += pasosahacer - Bpasosafavor + 1
				Opasosafavor += pasosahacer - Bpasosafavor + 1
				Bpasosafavor = 0
			else :
				pasosTotales += 1
				Bpasosafavor = 0
				Opasosafavor += 1

			BPos = int(ordenes[j+1])

		j+=2
	archsale.write("Case #"+ str(i) + ": " + str(pasosTotales) + "\n")
archsale.close()
archivo.close()

