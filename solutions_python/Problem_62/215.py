
def intersects(a,b,c,d):
	return a>=c and b<=d or a<=c and b>=d
	
def intersects_count(L):
	r = 0
	for i in xrange(len(L)):
		for j in xrange(i+1, len(L)):
			if intersects( L[i][0], L[i][1], L[j][0], L[j][1] ):
				r+=1
	return r
	
lines = open("A-large.in").read().split("\n")
T = int(lines[0])

output = []
line_index = 1

for t in xrange(1, T+1):
	n = int(lines[line_index])
	line_index+=1
	
	points = []
	for i in xrange(n):
		a, b = [int(x) for x in lines[line_index].split()]
		line_index+=1
		points.append((a,b,))
	
	r = intersects_count(points)
	
	result = "Case #"+str(t)+": " + str(r)
	output.append( result )
	
print "\n".join(output)
open("result.out", "w").write("\n".join(output))
		
