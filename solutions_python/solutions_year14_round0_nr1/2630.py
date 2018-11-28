for a in range(int(input(""))):
	rod = int(input(""))
	mogulegarTolur = []
	mogulegarTolur2 = []
	rettarTolur = []

	for b in range(4):
		tolur = input("")
		if b == rod-1:
			mogulegarTolur = [int(x) for x in tolur.split(" ")]

	rod = int(input(""))
	for b in range(4):
		tolur = input("")
		if b == rod-1:
			mogulegarTolur2 = [int(x) for x in tolur.split(" ")]

	for c in mogulegarTolur:
		if c in mogulegarTolur2:
			rettarTolur.append(c)

	if len(rettarTolur) == 1:
		print("Case #" + str(a+1) + ": " + str(rettarTolur[0]))
	elif len(rettarTolur) == 0:
		print("Case #" + str(a+1) + ": Volunteer cheated!")
	else:
		print("Case #" + str(a+1) + ": Bad magician!")