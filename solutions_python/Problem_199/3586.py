
f = open("A-large.in","r")
o = open("A-large-output.out","w")

t = int(f.readline())

def flip(c):
	if c == '-':
		return '+'
	else:
		return '-'

for i in range(t):
	inp = f.readline().split(" ")
	p = list(inp[0])
	k = int(inp[1])
	flips = 0

	for c in range(len(p)):
		if p[c] == '-':
			if c+k <= len(p):
			    for z in range(c,c+k):
				    p[z] = flip(p[z])
			flips = flips + 1

	if '-' in p:
		 o.write("Case #"+str(i+1)+": "+ "IMPOSSIBLE\n")
	else:
		o.write("Case #"+str(i+1)+": "+ str(flips)+"\n")

f.close()
o.close()