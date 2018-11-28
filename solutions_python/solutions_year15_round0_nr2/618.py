import sys
f,out = open("input", "r"),open("output", "w")
T = int(f.readline())
def div(x,d):
	y=x/d
	if y!=int(y):
		return int(y)+1
	return int(y)
for t in range(T):
	D = int(f.readline())
	P = [int(w) for w in f.readline().split()]
	x = max(P)
	for i in range(1,max(P)):
		y = 0
		for j in [k for k in P if k>i]:
			y += div(j,i) - 1
		if y+i<x:
			x=y+i
	out.write("Case #" + str(t+1) +": " + str(x) + "\n")