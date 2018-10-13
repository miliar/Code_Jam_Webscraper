def flip(p, k, i):
#	print(p)	
	for z in range(i, i+k):
		if p[z] == "+":
			p[z] = "-"
		else:
			p[z] = "+"
#	print(p)

def scan(p, k, s):
	count = 0
	for i in range(0, s - k + 1):
		if p[i] == "-":
			count += 1
			flip(p, k, i)
	return count

t = input()
for i in range(0, int(t)):
	line = input()
	p, k = line.split()
	p = list(p)
	s = len(p)
	k = int(k)
	
	count = 0
	if "-" in p:
		count = scan(p, k, s)
		if "-" in p:
			count = "IMPOSSIBLE"
	print("Case #" + str(i + 1) + ": " + str(count))
