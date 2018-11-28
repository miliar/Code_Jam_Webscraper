
def is_tidy(n):
	n_list = list(str(n))
	for i in range(len(n_list) - 1):
		if int(n_list[i]) > int(n_list[i+1]):
			return False
	return True


T = int(input())
for t in range(1, T+1):
	n = int(input())
	while True:
		if is_tidy(n):
			print("Case #{}: {}".format(t, n))
			break
		else:
			n -= 1