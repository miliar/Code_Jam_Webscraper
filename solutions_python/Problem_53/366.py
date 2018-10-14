f = file("A-large.in", "r")
of = file("A-large.out", "w")
lines = f.readlines()

cases = int(lines[0])
for i in range(cases):
	input = lines[i + 1].split(" ");
	n = int(input[0])
	k = int(input[1])
	
	nn = (2 ** n) - 1
	
	print "N=", n, "K=", k, "nn=", nn
	
	if k & nn == nn:
		of.write("Case #%i: ON\n" % (i + 1))
	else:
		of.write("Case #%i: OFF\n" % (i + 1))
	
