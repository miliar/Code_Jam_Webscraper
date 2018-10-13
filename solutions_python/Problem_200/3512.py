
def last_tidy(N):
	if N < 10:
		# Always tidy
		return N

	N_list = [int(x) for x in str(N)]

	for i in range(len(N_list)-1):
		if N_list[i] > N_list[i+1]:
			N_list[i] = N_list[i] - 1
			for j in range(i+1, len(N_list)):
				N_list[j] = 9
			n = int("".join([str(x) for x in N_list]))
			return last_tidy(n)

	n = int("".join([str(x) for x in N_list]))
	return n


T = int(input())

for i in range(1, T+1):
	N = int(input())

	print("Case #{}: {}".format(i, last_tidy(N)))