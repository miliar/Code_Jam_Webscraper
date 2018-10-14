import sys, math


def get_new_distances(stall_distance):
	if stall_distance%2 == 0:
		new_distances = [stall_distance/2, stall_distance/2 - 1]
	else:
		new_distances = [(stall_distance - 1)/2, (stall_distance - 1)/2]
	return new_distances

def add_new_distances(stall_distances, new_distances, n_stalls=1):
	for new_type in new_distances:
		if new_type not in stall_distances:
			stall_distances[new_type] = n_stalls
		else:
			stall_distances[new_type] += n_stalls


def choose_stall(N, K):
	if N == K:
		return '0 0'
	stall_distances = {N: 1}
	log_K = int(math.log(K,2))
	if log_K:
		K = K - 2**log_K
		while log_K > 0:
			keys = stall_distances.keys()
			for key in keys:
				n_stalls = stall_distances.pop(key)
				new_distances = get_new_distances(key)
				add_new_distances(stall_distances, new_distances, n_stalls)
			log_K -= 1
	max_stall = max(stall_distances.keys())
	min_stall = min(stall_distances.keys())
	if stall_distances[max_stall] > K:
		last_chosen = max_stall
	else:
		last_chosen = min_stall
	new_distances = get_new_distances(last_chosen)
	max_d = max(new_distances)
	min_d = min(new_distances)
	return '%d %d' %(max_d, min_d)

def solve_case(case, f, fout):
	N, K = f.readline().strip().split()
	N = int(N)
	K = int(K)
	result = choose_stall(N, K)
	write_line(fout, case, str(result))

def write_line(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	#input_file_name = 'test.in'
	input_file_name = sys.argv[1]
	
	f = file(input_file_name)
	fout = file("%s.out" %(input_file_name.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solve_case(case + 1, f, fout)
		
	f.close()
	fout.close()
