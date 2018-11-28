import sys

def parse(filename):
	cases = []
	n_cases = 0
	with open(filename,'r') as f:
		n_cases = int(f.readline())
		for i in range(n_cases):
			s_max, s = f.readline().split()
			cases.append((int(s_max),s))
	return n_cases, cases

def get_result_as_string(i, n_friends):
	return "Case #%i: %i\n"%(i+1, n_friends)

def get_n_friends(s_max, s):
	standing_up = 0
	friends = 0
	for p in range(s_max+1):
		if int(s[p]) > 0 and standing_up + friends < p:
			friends += p - standing_up - friends
		standing_up += int(s[p]) 
	return friends

if __name__ == "__main__":
	if len(sys.argv) > 1:
		n_cases, cases = parse(sys.argv[1])
		with open('lolilol.txt','w') as f:
			for i in range(n_cases):
				n_friends = get_n_friends(cases[i][0], cases[i][1])
				# print(get_result_as_string(i,n_friends)[:-1])
				f.write(get_result_as_string(i,n_friends))



