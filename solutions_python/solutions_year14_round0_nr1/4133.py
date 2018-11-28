magicin = open ('in.txt', 'r')
magicout = open('out.txt', 'w')
magic = []
count = magicin.readline()
count = count.split()
count = count[0]
count = int(count)

i = int(0)

while i < count:
	
	guess1line = []
	guess2line = []

	guess1 = magicin.readline()
	guess1 = guess1.split()
	guess1 = guess1[0]
	guess1 = int(guess1)

	print guess1

	guess1line = magicin.readline()
	guess1line = guess1line + magicin.readline()
	guess1line = guess1line + magicin.readline()
	guess1line = guess1line + magicin.readline()
	guess1line = guess1line.split()
	guess1line = guess1line[((guess1*4)-4):(guess1*4)]

	print guess1line

	guess2 = magicin.readline()
	guess2 = guess2.split()
	guess2 = guess2[0]
	guess2 = int(guess2)

	print guess2

	guess2line = magicin.readline()
	guess2line = guess2line + magicin.readline()
	guess2line = guess2line + magicin.readline()
	guess2line = guess2line + magicin.readline()
	guess2line = guess2line.split()
	guess2line = guess2line[((guess2*4)-4):(guess2*4)]


	print guess2line
	print "~~~~~~~"
	
	same = set(guess1line) & set(guess2line)
	same = list(same)
	print same
	case = i
	case = int(case)+int(1)
	if len(same)==0:
		magicout.write("Case #" + str(case) + ": " + "Volunteer cheated!" + "\n")
	if len(same)==1:
		magicout.write("Case #" + str(case) + ": " + str(same[0]) + "\n")
	if len(same)>1:
		magicout.write("Case #" + str(case) + ": " + "Bad magician!" + "\n")

	i = i + 1
