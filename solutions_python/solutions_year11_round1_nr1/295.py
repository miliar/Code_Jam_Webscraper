import sys

lines = sys.stdin.read().split('\n')
T = int(lines[0])
for i in range(1,T+1):
	dat = lines[i].split(' ')
	N  = int(dat[0])
	PD = int(dat[1])/100
	PG = int(dat[2])/100
	result = "Broken"
	if (PG != 1 or PD == 1) and (PG != 0 or PD == 0):
		for j in reversed(range(1,N+1)):
			#print(PD*j-int(PD*j))
			if PD*j-int(PD*j) == 0:
				result = "Possible"
				break;
	
	print("Case #%d: %s" % (i,result))
	
