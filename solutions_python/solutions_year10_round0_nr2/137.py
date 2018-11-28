# Sigh, it had an error when the answer was 0
# Sigh...

filename = "B-large.in"
data = [line for line in open(filename).read().split("\n")][0:-1]
data = [[int(x) for x in line.split(" ")] for line in data]

t = data[0][0]
data = data[1:]

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a%b)

for x in range(0, len(data)):
	n = len(data[x]) - 1
	planets = sorted(data[x][1:])
	#print n, planets
	deltas = [planets[y] - planets[y-1] for y in range(1, len(planets))]
	GCD = deltas[0]
	#print deltas
	for y in range(1, len(deltas)):
		GCD = gcd(GCD, deltas[y])
	#print GCD
	print "Case #%d: %d" % (x+1, (GCD - planets[0] % GCD) % GCD)

