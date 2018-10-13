from sys import argv


def calc_income(runs, space, groups):
	income = 0
	for i in range(runs):
		inds = 0
		for j in range(len(groups)):
			if(inds+groups[j] <= space):
				inds += groups[j]
				income += groups[j]
			else:
				tmp = groups[:j]
				groups[:j] = []
				groups.extend(tmp)
				break
	return income	

if __name__ == '__main__':
	file = open(argv[1])
	tests = int(file.readline())
	for i in range(tests):
		rkgs = file.readline().split()
		r, k = int(rkgs[0]), int(rkgs[1])
		groups = file.readline().split()
		groups_int = [int(x) for x in groups]
		print("Case #%i: %i"%(i+1, calc_income(r,k, groups_int)))


		
	
