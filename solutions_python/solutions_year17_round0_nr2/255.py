T = int(raw_input())

def doprob():
#"""	x = list(str(raw_input()))
#	outstack = [(0,0)]
#	ctr = 0
#	current = 0 # unneeded
#	while ctr < len(x):
#		current, index = outstack[-1]
#		if x[ctr] > current:
#			outstack.append((x[ctr],ctr))
#		elif x[ctr] == current:
#			pass # outstack[-1] = (current, ctr)
#		else:
#			outstack[-1] = (current-1, index)
#			outstack.append('9',len(x)-1)
#			return parse(outstack[1:], len(x))
#		ctr += 1
#	return parse(outstack[1:], len(x))"""
	x = list(raw_input())
	out = "0"
	current = '0'
	for c in x:
#		print out, "asdf"
		if c >= current:
			out = out + c
			current = c
		else:
			while out[-1] == current:
				out = out[:-1]
			out = out + str(int(current)-1)
			out = out + (1+len(x) - len(out))*'9'
			break
	while out[0] == '0':
		out = out[1:]
	return out


for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())