filename = "A-large.in"
outf = file("out.out", "w")
rows = [i.strip() for i in file(filename).readlines()][1::]

i = 1

def calc1(s,k,step):
	curr_s = s
	step = 0
	while (True):
		s = s.strip('+')
		if (len(s) == 0):
			return str(step)
		
		if (len(s) < k):
			return 'IMPOSSIBLE'
		#where 
		if (s[:k:].count("-") > s[-k:0:].count("-")):
			to_flip = s[:k:]
			s = s[k::]
			to_flip = to_flip.replace("+", "a").replace("-", "+").replace("a", "-")
			s = to_flip + s
			step += 1
		else:
			to_flip = s[-k:0:]
			s = s[:-k:]
			s = s + to_flip
			step += 1


def calc(s,k,step):
	s = s.strip('+')
	if (len(s) == 0):
		return step
	
	if (len(s) < k):
		return 'IMPOSSIBLE'
	#where 
	if (s[:k:].count("-") > s[-k:0:].count("-")):
		to_flip = s[:k:]
		s = s[k::]
		to_flip = to_flip.replace("+", "a").replace("-", "+").replace("a", "-")
		return str(calc(to_flip + s, k, step+1))
	else:
		to_flip = s[-k:0:]
		s = s[:-k:]
		to_flip = to_flip.replace("+", "a").replace("-", "+").replace("a", "-")
		return str(calc(s + to_flip, k, step+1))



for row in rows:
	s,k = row.split(' ')
	k = int(k)
	outf.write("Case #" + str(i) + ": " + str(calc1(s,k,0)) + "\n")
	i += 1
