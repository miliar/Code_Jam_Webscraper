def do_case():
	# input()
	# int(input())
	d, n = list(map(int, input().split()))
	horses = [list(map(int, input().split())) for _ in range(n)]

	time = []
	for k, s in horses:
		time.append((d-k) / s)
	return d / max(time)

T = int(input())
for case in range(T):
	ans = do_case()
	print("Case #{}: {}".format(case+1, ans))
