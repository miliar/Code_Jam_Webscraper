import sys

def winner(x,r,c):
	newc = min(r,c)
	newr = max(r,c)
	if(x > 2):
		smallside = ((x-1) // 2) + 1
		longside = x  - smallside + 1
	else:
		smallside = 1
		if(x == 2):
			longside = 2
		else:
			longside = 1
#	print smallside, longside 
	if((r * c) % x != 0):
		return "RICHARD"
	elif(x >= 7):
		return "RICHARD"
	elif((smallside > newc) | (longside > newr)):
		return "RICHARD"
	elif((smallside == newc) &(longside > newc) & (newr >= 3) & (x >= 4)):
		return "RICHARD"
	else:
		return "GABRIEL"

def main():
	cases = int(sys.stdin.readline())
	for i in range(cases):
		param = sys.stdin.next().split()
		param[0] = int(param[0])
		param[1] = int(param[1])
		param[2] = int(param[2])
		print "Case #%d:" % (i+1), winner(param[0],param[1],param[2])			

if __name__ == '__main__':
	main()