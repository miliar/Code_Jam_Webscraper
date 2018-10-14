import math

def pal(i):
	return str(i) == str(i)[::-1]

casesLen = int(raw_input())

cases = []

for i in range(casesLen):
	start,end = raw_input().split(' ')
	cases.append( { "start": int(start), "end": int(end) } )

for i in range(casesLen):
	pals = 0
	j = int(math.floor(math.sqrt(cases[i]["start"])))
	while j*j <= cases[i]["end"]:
		if j*j >= cases[i]["start"] and pal(j) and pal(j*j):
			pals = pals + 1
		j = j+1
	print "Case #{}: {}".format(i+1,pals)
