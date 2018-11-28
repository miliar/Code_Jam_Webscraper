fin = open("in.txt", "r")
fout = open("out.txt", "w")

T = int(fin.readline())
for i in range(T):
	vs = fin.readline().split()
	N = int(vs[0])
	S = int(vs[1])
	p = int(vs[2])
	ans = 0
	for j in range(3, len(vs)):
		score = int(vs[j])
		s0 = False
		s1 = False
		#print(score)
		for x in range(score+1):
			for y in range(x, score+1):
				z = score - x - y
				if z < y or z < p:
					break
				if z - x <= 1:
					s0 = True
					#print(x, y, z)
				if z - x == 2:
					s1 = True
					#print(x, y, z)
		if s0:
			ans += 1
		else:
			if s1 and S > 0:
				S -= 1
				ans += 1
	fout.write("Case #" + str(i+1) + ": " + str(ans) + "\n")