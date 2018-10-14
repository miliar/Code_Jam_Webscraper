import bisect
INPUT_FILE = 'C-small-1-attempt0.in'
OUTPUT_FILE = 'C-small-attempt0_out.txt'

def solve(f_in):
	lstVars = f_in.readline().strip().split(' ')
	N = int(lstVars[0])
	K = int(lstVars[1])
	places = [0, N + 1]
	min_s = -1
	max_s = -1
	for i in range(K):
		min_s = -1
		max_s = -1
		selected_s = -1
		
		for j in range(len(places) - 1):
			Left = places[j]
			Right = places[j + 1]
			S = (Left + Right) / 2
			Ls = S - Left - 1
			Rs = Right - S - 1
			if min_s < min(Ls, Rs):
				min_s = min(Ls,Rs)
				max_s = max(Ls,Rs)
				selected_s = S
			elif min_s == min(Ls,Rs):
				if max_s < max(Ls,Rs):
					max_s = max(Ls,Rs)
					selected_s = S
		bisect.insort(places, selected_s) 
	return str(max_s) + " " + str(min_s)

with open(INPUT_FILE, 'r') as f:
	with open(OUTPUT_FILE, 'w') as f_out:
		T = int(f.readline())
		for i in range(T):
			f_out.write('Case #%d: %s\n'%(i + 1, solve(f)))
				