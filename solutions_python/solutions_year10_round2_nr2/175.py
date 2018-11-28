f = file("B-large.in", "r")
of = file("B-large.out", "w")
lines = f.readlines()

cases = int(lines[0])
line = 1
for case in range(cases):
	input = lines[line].split(" ")
	n = int(input[0])
	k = int(input[1])
	b = int(input[2])
	t = int(input[3])
	
	print "n", n, "k", k, "b", b, "t", t
	
	line += 1
	pos = lines[line].split(" ")
	line += 1
	vel = lines[line].split(" ")
	line += 1

	print pos
	print vel
	
	safe = 0
	chick = n - 1
	last = False
	while chick >= 0 and not last:
		if int(pos[chick]) + int(vel[chick]) * t >= b:
			safe += 1
		else:
			last = True

		chick -= 1
		
	print "safe", safe	
	
	swaps = 0
	slowers = 1
	while safe < k and chick >= 0:
		if int(pos[chick]) + int(vel[chick]) * t >= b:
			print "ok, but costs", slowers
			swaps += slowers
			safe += 1
		else:
			print "slower"
			slowers += 1
			
		chick -= 1
		
	if safe >= k:
		of.write("Case #%d: %d\n" % (case + 1, swaps))
	else:
		of.write("Case #%d: IMPOSSIBLE\n" % (case + 1))