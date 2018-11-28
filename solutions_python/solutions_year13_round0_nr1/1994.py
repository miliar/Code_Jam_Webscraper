def check(line):
	last = None
	c = 0
	if line == "TTTT":
		return False,'T'
	for y in line: 
		if last == None:
			last = y
			c += 1
		elif y != '.' and (last == y or last == "T" or y == "T" ):
			if last == 'T':
				last = y
			else:
				last = last
			c += 1
		else:
			break
	return c == 4,last

def main(t):
	T = input(),input(),input(),input()
	input()	
	
	emptySomewhere = False
	diag1 = (T[i][i] for i in range(4)),
	diag2 = (T[3-i][i] for i in range(4)),
	for case in T,zip(*T),diag1,diag2:
		for line in case:
			won,who = check(line)
			if won:
				print("Case #{0}: {1} won".format(t+1,who))
				return
			if not emptySomewhere:
				emptySomewhere = "." in line
	if emptySomewhere:
		print("Case #{0}: Game has not completed".format(t+1))
	else:
		print("Case #{0}: Draw".format(t+1))

Nt = int(input())
for t in range(Nt):
	main(t)
