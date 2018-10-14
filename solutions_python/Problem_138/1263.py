infile = open("D-large.in", "r")
f = open('outpu.txt', 'w')
cases = infile.read().strip().split("\n")
nb_cases = cases[0][0]
cases = cases[1:]
i = 0
j = 1
for case in cases: 
	if i % 3 != 0:
		for char in case:
			if char == " ":
				if adding_to == "tableNaomi":
					tableNaomi.append(string_to_add)
				else:
					tableKen.append(string_to_add)
				string_to_add = ""
			else:
				string_to_add = string_to_add + char
		if adding_to == "tableNaomi":
			tableNaomi.append(string_to_add)
		else:
			tableKen.append(string_to_add)
		if adding_to == "tableNaomi":
			string_to_add = ""
			adding_to = "tableKen"
		else:
			tableNaomiWar = tableNaomi
			tableKenWar = tableKen
			tableNaomiDec = list(tableNaomi)
			tableKenDec = list(tableKen)
			while len(tableNaomiWar) != 0:
				naomi_play = min(tableNaomiWar)
				ken_plays = [ken_plays for ken_plays in tableKenWar if ken_plays > naomi_play]
				if len(ken_plays) > 0:
					ken_play = min(ken_plays)
				else:
					ken_play = min(tableKenWar)
				if ken_play < naomi_play:
					naomiWarPoints = naomiWarPoints + 1
				tableNaomiWar.remove(naomi_play)
				tableKenWar.remove(ken_play)
			while len(tableNaomiDec) != 0:
				if max(tableNaomiDec) < max(tableKenDec):
					naomi_choice = float(max(tableKenDec)) - 0.001
					naomi_play = min(tableNaomiDec)
					tableNaomiDec.remove(naomi_play)
					ken_play = max(tableKenDec)
					tableKenDec.remove(ken_play)
				else:
					naomi_play = max(tableNaomiDec)
					tableNaomiDec.remove(naomi_play)
					ken_play = max(tableKenDec)
					tableKenDec.remove(ken_play)
					naomiDecPoints = naomiDecPoints + 1
			print >> f, "Case #%s: %s %s" % (j, naomiDecPoints, naomiWarPoints)
			j = j + 1

	else:
		naomiDecPoints = 0
		naomiWarPoints = 0
		string_to_add = ""
		tableNaomi = []
		tableKen = []
		adding_to = "tableNaomi"
	i = i + 1
	