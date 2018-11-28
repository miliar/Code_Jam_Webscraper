from random import uniform as rr

def solve(c,f,x):
	def running_time():
		i = 0
		total = 0
		while True:
			total += c/(2+i*f)
			yield total
			i += 1
	old_time = x/2
	new_time = None
	i = 1
	for run_time in running_time():
		new_time = x/(2+i*f) + run_time
		if new_time > old_time:
			return old_time
		old_time = new_time
		i += 1

def get_input(fn):
	with open(fn) as f:
		T = int(f.readline())
		tests = [map(float,f.readline().split()) for _ in range(T)]
		return tests

def rand_tests():
	tests = []
	for i in range(1000):
		tests.append([rr(1.0,10000.0), rr(1.0,4.0), rr(1.0,100000.0)])
	return tests

if __name__ == '__main__':
	tests = get_input('pb.in')
	out = open('pb.out', 'w')
	for i in range(len(tests)):
		out.write("Case #{}: {:.7f}\n".format(i+1,solve(*tests[i])))
	out.close()
