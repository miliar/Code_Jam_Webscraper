import sys
f = open(sys.argv[1])
f2 = open("res.txt", "w")

for index in range(int(f.readline().strip())):
	s, arr = f.readline().strip().split(" ")
	arr = map(int, arr)
	counter = 0
	missing = 0
	for x in arr:
		counter += x - 1
		if counter < 0:
			counter = 0
			missing += 1
	f2.write("Case #{n}: {m}\n".format(n=index+1, m=missing))
