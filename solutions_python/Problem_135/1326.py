

def solve(ans1 , card1 , ans2 , card2):
	ans1 = card1.split('\n')[int(ans1) - 1]
	ans2 = card2.split('\n')[int(ans2) - 1]
	print card2
	print ">>" ,ans2
	found = False
	num = ""

	for x in ans2.split():
		print "x" , x
		if x in ans1:
			num = x
			if found:
				return "Bad magician!"

			else:
				found = True


	if found:
		return num
	else :
		return "Volunteer cheated!"


def solve2(ans1 , card1 , ans2 , card2):
	a1 = card1.strip(" ").split('\n')[int(ans1) - 1]
	a2 = card2.strip(" ").split('\n')[int(ans2) - 1]

	tot = set(a1.split())
	num = 0
	
	for x in a2.split():
		sz = len(tot)
		tot.add(x)
		if (sz == len(tot)):
			num = x	

	if len(tot) == 8:
		return "Volunteer cheated!"
	elif len(tot) == 7:
		return num
	else:
		return "Bad magician!"


# print solve("2" , "1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16" , "3" , "1 2 5 4\n3 11 6 15\n9 10 7 12\n13 14 8 16")
# print solve("2" , "1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16" ,"2" , "1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16" )
# print solve("2" , "1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16" , "3" , "1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16")


fin = open(r"C:\Documents and Settings\Administrator\My Documents\Downloads\A-small-attempt2(1).in")
fout = open(r"out\test12.out" , "w")

l = int(fin.readline().rstrip('\n'))

for x in xrange(l):
	ans1 = fin.readline().rstrip('\n')
	card1 = ""
	for j in xrange(4):
		card1 = card1 + fin.readline()

	ans2 = fin.readline().rstrip('\n')

	card2 = ""
	for j in xrange(4):
		card2 = card2 + fin.readline()	


	fout.writelines("Case #"+ str( x + 1) + ": "+ solve2(ans1 , card1 , ans2 , card2)+"\n")
	fout.flush()


fin.close()
fout.close()

