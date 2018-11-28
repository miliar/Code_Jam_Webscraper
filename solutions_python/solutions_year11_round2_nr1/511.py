#infile = "input.txt"

#infile = "A-small-attempt1.in"
infile = "A-large.in"
input = open(infile, "r")
outfile = "B.txt"
output = open(outfile, "w")


test_cases = input.readline().rstrip("\n")
test_cases = int(test_cases)



for t in range(1, (test_cases+1)):
	WPs = []
	OWPs = []
	OOWPs = []

	team_scores = []
	team_wins_losses = []
	line = input.readline().rstrip("\n")
	N = int(line)
	for i in range(0, N):
		wins = 0
		losses = 0
		scores = input.readline().rstrip("\n")

		for item in scores:
			if item == "1":
				wins = wins+1
			if item == "0":
				losses = losses+1
			if wins+losses != 0:
				WP = float(wins)/float(wins+losses)
			else:
				WP = 0

		WPs.append(WP)
		team_scores.append(scores)	

	for i in range(0, N):
		OWP = 0
		played_against = 0
		for k in range(0, N):
			wins = 0
			losses = 0
			if k != i:
				scores = team_scores[k]
				if scores[i] != ".":
					played_against = played_against + 1
					for j in range(0, N):
						item = scores[j]
						if j != i:
							if item == "1" or item == "0":
								if item == "1":
									wins = wins+1
								if item == "0":
									losses = losses+1
					if wins+losses != 0:
						WP = float(wins)/float(wins+losses)
					else:
						WP = float(0)
					OWP = float(OWP) + float(WP)
		OWP = float(OWP) / float(played_against)
		OWPs.append(OWP)		

	for i in range(0, N):
		OOWP = 0
		played_against = 0
		for k in range(0, N):
			if k != i:
				scores = team_scores[k]
				if scores[i] != ".":
					played_against = played_against + 1
					OOWP = float(OOWP) + float(OWPs[k])
		OOWP = float(OOWP)/float(played_against)
		OOWPs.append(OOWP)	

	number = t
	number = str(number)
	output.write("Case #"+number+":\n")
	for i in range(0, N):
		WP = float(WPs[i])
		OWP = float(OWPs[i])
		OOWP = float(OOWPs[i])
		RPI = (0.25*WP)+(0.50*OWP)+(0.25*OOWP)
		output.write(str(RPI))
		output.write('\n')


input.close()
output.close()
