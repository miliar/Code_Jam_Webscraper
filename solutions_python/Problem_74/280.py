def read_data(f):
	s = file(f).read().splitlines()[1:]
	s = [x.split(" ")[1:] for x in s]
	tests = []
	for test in s:
		res = []
		for i in xrange(0,len(test),2):
			if test[i] == 'O':
				res.append((0,int(test[i + 1])))
			else:
				res.append((1,int(test[i + 1])))
		tests.append(res)
	return tests

def solve(points):
	pos = [1,1]
	extra_time = [0,0]
	total_time = 0
	for point in points:
		move_time = (max(abs(point[1] - pos[point[0]]) - extra_time[point[0]],0) + 1)
		total_time += move_time
		pos[point[0]] = point[1]
		extra_time[point[0]] = 0
		extra_time[1 - point[0]] += move_time
	return total_time

def solve_all(inp, out):
	data = read_data(inp)
	res = []
	for d in data:
		res.append(solve(d))
	f = file(out,"w")
	for i,r in enumerate(res):
		f.write("Case #%d: %d\n"%(i+1,r))
	f.close()
