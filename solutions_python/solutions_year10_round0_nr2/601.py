
#lines = open("b_test1.in").read().split("\n")
#lines = open("B-small-attempt0.in").read().split("\n")
#lines = open("B-small-attempt1.in").read().split("\n")
#lines = open("B-small-attempt2.in").read().split("\n")
#lines = open("B-small-attempt3.in").read().split("\n")
#lines = open("B-small-attempt4.in").read().split("\n")
#lines = open("B-small-attempt5.in").read().split("\n")
#lines = open("B-small-attempt6.in").read().split("\n")
lines = open("B-large.in").read().split("\n")



def dv(a, b):
	if a < b: return dv(b, a)
	elif b==0: return a
	else: return dv(b, a % b)

C = int(lines[0])
#print C 
output = []
for i in xrange(1, C+1):
	t = [ int(x) for x in lines[i].split()[1:] ]
	#unique
	d = {}
	for x in t:
		d[x] = True
	r = list(sorted(d.keys()))
	#print r
	r = [ abs(a-b) for a,b in zip(r[1:], r[:-1]) ]
	
	T = reduce(dv, r)
	y = T - t[0]%T
	if T==y:
		y = 0
	output.append('Case #'+str(i)+': ' +str(y))
	print T, y
	#print i, ':', T, y

open("b.out", "w").write("\n".join(output))
#print "\n".join(output)