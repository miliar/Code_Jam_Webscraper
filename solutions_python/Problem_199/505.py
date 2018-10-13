import fileinput

# takes a list of booleans and the size of the flipper
def solve(cakes, k):
	# Remove True values in the beginning
	firstFalseAt = cakes.index(False)
	if firstFalseAt != 0:
		cakes = cakes[firstFalseAt:]

	# Long enough?
	if len(cakes) < k:
		return None

	# Flip first k
	for x in range(k):
		cakes[x] = not cakes[x]

	return cakes

count = None
case = 0
for line in fileinput.input():
	line = line.rstrip()
	if count is None:
		count = int(line)
		continue
	case += 1

	pancakes, k = line.split()
	pancakes = [c == "+" for c in pancakes]
	k = int(k)

	flipcounter = 0
	while True:
		if False not in pancakes:
			print "Case #%s: %s" % (case, flipcounter)
			break
		pancakes = solve(pancakes, k)
		flipcounter += 1
		if pancakes == None:
			print "Case #%s: IMPOSSIBLE" % case
			break
