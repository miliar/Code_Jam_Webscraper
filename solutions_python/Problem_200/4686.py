nbTests = int(input())

def trouverMax(nombre):
	for i in range(len(nombre)-1, 0, -1):
		if i == 1:
			if nombre[i] < nombre[i-1]:
				nombre[0] = str(int(nombre[0])-1)
				for j in range(len(nombre)-1):
					nombre[j+1] = "9" 
		else:
			if nombre[i] < nombre[i-1]:
				nombre[i] = "9"
				nombre[i-1] = str(int(nombre[i-1])-1)

	return nombre




for i in range(1, nbTests+1):
	nombre = list(input())
	
	nombreRange = int("".join(trouverMax(nombre)))

	print("Case #{}: {}".format(i, nombreRange))