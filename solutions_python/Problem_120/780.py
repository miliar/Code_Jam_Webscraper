def paintForRad(rad):
	return ((rad + 1) ** 2) - rad ** 2

size = "small"
attempt = "2"

f = open("A-{}-attempt{}.in".format(size, attempt), "r")
out = file("{}.out".format(size), "w")

lines = f.read().splitlines()[1:]

cases = []
output = []

for i in range(0, len(lines)):
	cases.append([int(x) for x in lines[i].split(" ")])

currentCase = 1

for case in cases:
	r = case[0]
	paint = case[1]
	circles = 0

	while True:
		currentPaint = paintForRad(r)

		if paint - currentPaint >= 0:
			paint -= currentPaint
			r += 2
			circles += 1
		else:
			break

	output.append(circles)
	#print circles

for outNum in range(len(output)):
	out.write("Case #{0}: {1}\n".format(outNum + 1, output[outNum]))