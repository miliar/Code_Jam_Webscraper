ip_file = "input.txt"
op_file = "output.txt"

with open(ip_file, 'r') as ifp:
	t = int(ifp.readline())
	with open(op_file, 'w+') as ofp:
		for nt in xrange(t):
			s = list(ifp.readline().strip())
			flag = True
			s_len = len(s)
			o = ""
			# print nt + 1
			# print s
			if len(s) == 1:
				o = "".join(s).lstrip("0")
				ofp.write("Case #{}: {}\n".format(nt + 1, o))
				continue
			for idx in xrange(s_len - 1):
				# print s[idx] + "   " + s[idx + 1]
				if s[idx] == "1" and s[idx + 1] == "0":
					o = "9" * (s_len - 1)
					break
				elif int(s[idx]) > int(s[idx + 1]):
					if len(o) != 0 and o[-1] == s[idx]:
						o = list(o)
						for oidx in xrange(len(o)):
							o[oidx] = str(int(o[oidx]) - 1)
						o = "".join(o)
						o += "9" * (s_len - len(o))
					else:
						o += str(int(s[idx]) - 1) + "9" * (s_len - idx - 1)
					break
				else:
					o += s[idx]
					# print str(idx) + "   " + str(s_len)
					if idx + 1 == s_len - 1:
						o += s[idx + 1]
			ofp.write("Case #{}: {}\n".format(nt + 1, o.lstrip("0")))