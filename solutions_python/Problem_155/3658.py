n = raw_input()
for i in range(int(n)):
	audiance = raw_input().split(" ")[1]
	ustalo = int(audiance[0])
	res = 0
	for a in range(1, len(audiance)):
		if ustalo >= a:
			ustalo += int(audiance[a])
		elif ustalo < a and audiance[a] != '0':
			res += a - ustalo
			ustalo += res + int(audiance[a])

	print ("Case #%d: %d") % (i+1, res)