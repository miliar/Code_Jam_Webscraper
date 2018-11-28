def friends_needed(s_max, aud):
	res = 0
	n_clapping = 0
	#nc = []
	for i in xrange(0, s_max + 1):
		f = max(i - n_clapping, 0)
		res += f
		n_clapping += aud[i] + f
		#nc.append(str(n_clapping))
	#print " ".join(nc)
	return res


inf = open("ina.txt", 'r')
outf = open("outa.txt", 'w')

t = int(inf.readline())
for k in xrange(0, t):
	s_max, aud = inf.readline().split()	
	s_max = int(s_max)
	aud = map(int, list(aud))		
	outf.write("Case #" + str(k + 1) + ": ")	
	outf.write(str(friends_needed(s_max, aud)) + "\n")
outf.close()
