def read_set(path):
	s = file(path,"rb").read()
	ss = s.splitlines()
	t = eval(ss[0])
	inps = [(int(x.split(" ")[0]),int(x.split(" ")[1])) for x in ss[1:]]
	return t, inps

def check_light(n,k):
	if (n == 0):
		return 1
	return (k & ((1 << n) - 1)) == ((1 << n) - 1)

def solve(path_in,path_out):
	s = read_set(path_in)
	res = [check_light(*x) for x in s[1]]
	solution = ''.join(["Case #" + str(i + 1) + ": " + ["OFF","ON"][res[i]] + "\n" for i in range(len(res))])
	f = file(path_out,"w")
	f.write(solution)
	f.close()
	return solution
