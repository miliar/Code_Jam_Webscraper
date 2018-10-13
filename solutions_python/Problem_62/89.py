import sys

def intersects(w1, w2):
	da = w1[0] - w2[0]
	db = w1[1] - w2[1]
	return da*db < 0

def intersections(wire, visited):
	count = 0
	for v in visited:
		if intersects(wire, v):
			count += 1
	return count

def f(N, wires):
	visited = []
	count = 0
	for wire in wires:
		count += intersections(wire, visited)
		visited.append(wire)
	return count

inf = open(sys.argv[1])
T = int(inf.readline())
for i in range(T):
	N = int(inf.readline().strip())
	wires = []
	for j in range(N):
		wire = [int(x) for x in inf.readline().split()]
		wires.append(wire)
	result = f(N,wires)
	print "Case #%d: %d" % (i+1, result)
