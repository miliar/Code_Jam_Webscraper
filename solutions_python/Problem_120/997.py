def rings(r, t):
	# return (t - 1) / 4 - r / 2 + 1 - 1
	numberOfRings = 0
	cumArea = 0
	while cumArea <= t:
		numberOfRings +=1
		a = 2 * numberOfRings - 2
		cumArea += (2 * (r + a) + 1)
		# print(numberOfRings, cumArea)

	return numberOfRings - 1

# print(rings(1, 9))
# print(rings(1, 10))
# print(rings(3, 40))
# print(rings(1, 1000000000000000000))

numberOfLines = 0
for line in open('1A-small-attempt0.in'):
	if numberOfLines > 0:
		values = line.strip().split()
		result = rings(int(values[0]), int(values[1]))
		print('Case #' + str(numberOfLines) + ': ' + str(result))
	numberOfLines += 1