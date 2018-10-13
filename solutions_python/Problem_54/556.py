def read_set(path):
	s = file(path,"rb").read()
	ss = s.splitlines()
	c = eval(ss[0])
	inps = [map(long,x.split(" ")[1:]) for x in ss[1:]]
	return c, inps


def gcd_many(l):
	while 0 in l:
		l.remove(0)
	if 1 in l:
		return 1
	if len(l) == 1:
		return l[0]
	else:
		a = min(l)
		l = [x % a for x in l] + [a]
		return gcd_many(l)

def solve_one_inp(l):
    a = min(l)
    l = [x - a for x in l]
    while 0 in l:
        l.remove(0)
    if len(l) == 0:
        return a
    g = gcd_many(l)
    return (-a) % g

def solve(path_in,path_out):
	s = read_set(path_in)
	inps = s[1]
	res = [solve_one_inp(x) for x in s[1]]
	solution = ''.join(["Case #" + str(i + 1) + ": " + str(res[i]) + "\n" for i in range(len(res))])
	f = file(path_out,"w")
	f.write(solution)
	f.close()
	return solution
