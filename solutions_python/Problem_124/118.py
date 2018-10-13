triangles = []
total = 0
for i in range(10**6):
	total += i
	if i%2 == 1:
		triangles.append(total)

def fact(x):
	total = 1
	while x:
		total *= x
		x -= 1
	return total

def choose(n, k):
	return fact(n)/(fact(k)*fact(n-k))

def prob(diamonds, X, Y):
	dist = abs(X)+Y
	#Is triangle big enough?
	index = 0
	while diamonds > triangles[index]:
		index += 1
	#print index
	if dist/2 > index:
		return 0.
	if dist/2 < index:
		return 1.
	#Is space on y-axis?
	if X == 0:
		if diamonds < triangles[Y/2]:
			return 0.
		else:
			return 1.
	edge_diamonds = diamonds - triangles[index-1]
	if edge_diamonds > (index*2)+Y:
		return 1.0
	p = 0
	for i in range(Y+1):
		p += choose(edge_diamonds, i)*(0.5**edge_diamonds)
	return 1 - p

#result = prob(1, 0, 0)
#print result
#result = prob(1, 0, 2)
#print result
#result = prob(3, 0, 0)
#print result
#result = prob(3, 2, 0)
#print result
#result = prob(3, 1, 1)
#print result
#result = prob(4, 1, 1)
#print result
#result = prob(4, 0, 2)
#print result

f = open("Output.txt", 'w')
g = open("B-small-attempt0.in")
#g = open("Test.txt")
cases = g.readline()
for i in range(int(cases)):
	case = g.readline()
	diamonds, X, Y = case.split()
	print diamonds, X, Y
	result = prob(int(diamonds), int(X), int(Y))
	f.write("Case #" + str(i+1) + ": " + str(result))
	f.write("\n")

