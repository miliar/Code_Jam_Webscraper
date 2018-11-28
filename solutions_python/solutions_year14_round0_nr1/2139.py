
ficheiro=open(file_name,"r").read().split('\n');

for temp in range(1,int(ficheiro[0])+1):
	aux = int(ficheiro[1 + 10*(temp - 1 )])
	aux2 = int(ficheiro[1 + 10*(temp-1) + 5])
	aux = ficheiro[1 + 10*(temp - 1 ) + aux].split(' ')
	aux2 = ficheiro[1 + 10*(temp-1) + 5 + aux2].split(' ')
	collumn = set(aux)
	row = set(aux2)
	aux3 = row & collumn
	if len(aux3) > 1:
		aux4 = "Case #"+str(temp)+": Bad magician!"
		print(aux4)
	if len(aux3) == 1:
		for aux in aux3:
			aux4 = "Case #"+str(temp)+": "+str(aux) 
			print(aux4)
	if len(aux3) == 0:
		aux4 = "Case #"+str(temp)+": Volunteer cheated!" 
		print(aux4)

	
