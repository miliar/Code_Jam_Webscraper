import sys
fn = sys.argv[1]
fo = sys.argv[2]

f = open(fn).read().splitlines()
fOut = open(fo, 'w')
cases = int(f[0])
cur_line = 1

for case in xrange(cases):
	standing = 0
	additionS0 = 0
	sMax, counts = f[cur_line].split(" ")
	cur_line+=1

	counts = [int(n) for n in counts]
	for shyness, n in enumerate(counts):
		if n > 0:
			if shyness > standing:
				addition = shyness - standing
				additionS0 += addition
				standing += addition
			standing += n

	fOut.write("Case #{}: {}\n".format(case + 1, additionS0))