from sys import stdin
n = int(stdin.readline())

def readrow(r):
	rows = ["","","",""]
	for i in range(4):
		rows[i]=stdin.readline();
	return set(rows[r-1].split())

for i in range(n):
	choice = int(stdin.readline());
	elems = readrow(choice)
	result = elems.intersection(readrow(int(stdin.readline())))
	print "Case #%d:" % (i+1),
	if len(result)==1: print result.pop()
	elif len(result)==0: print "Volunteer cheated!"
	else: print "Bad magician!"
	


