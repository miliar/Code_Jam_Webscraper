import math
f = open('file.in', 'r')
data = f.readlines()
for i in range(1, len(data)):
	#data[i] = data[i][:-1]
	args = data[i].split()
	A = int(args[0]); B = int(args[1])
	val = A; ans = 0
	while val <= B:
		d = int(math.ceil(math.log10(val)))
		n = str(val);
		st = set()
		for pos in range(1, d):
			gen = ''
			for j in range(d):
				gen += n[(pos + j) % d]
			gen = str(int(gen))
			if len(gen) == len(n) and int(n) < int(gen) and int(gen) >= A and int(gen) <= B and gen not in st:
				ans += 1; st.add(n); st.add(gen);
		val += 1

	print "Case #" + str(i) + ": " + str(ans)
