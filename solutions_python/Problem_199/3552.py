ip_file = "input.txt"
op_file = "output.txt"

with open(ip_file, 'r') as ifp:
	t = int(ifp.readline())
	with open(op_file, 'w+') as ofp:
		for nt in xrange(t):
			s, k = ifp.readline().split()
			k = int(k)
			s = list(s)
			s_len = len(s)
			ncount = s.count('-')
			# print nt + 1
			if ncount == 0:
				ofp.write("Case #{}: 0\n".format(nt + 1))
			else:
				flips = 0
				flag = False
				per_flip = -1
				idx1 = 0
				while idx1 < s_len:
					if idx1 > s_len - k and s[idx1] == '-':
						flag = True
						break
					elif s[idx1] == '+':
						idx1 += 1
						continue
					for idx2 in xrange(idx1, idx1 + k):
						if s[idx2] == '-':
							s[idx2] = '+'
						else:
							s[idx2] = '-'
							if per_flip < 0:
								per_flip = idx2
						# print str(idx1) + "   " + str(flips) + "  " + str(s)
					if per_flip < 0:
						per_flip = idx1 + k
					idx1 = per_flip
					per_flip = -1
					flips += 1
				if flag:
					ofp.write("Case #{}: IMPOSSIBLE\n".format(nt + 1))
				else:
					ofp.write("Case #{}: {}\n".format(nt + 1, flips))