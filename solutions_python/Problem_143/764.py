def solve():
	(A, B, K) = (int(x) for x in input().split())

	ct = 0

	if (A > B):
		tmp = A
		A = B
		B = tmp

	for a in range(0, A):
		for b in range(0, B):
			if (a&b) < K:
				ct += 1
			# print(a, "-", b)

	print("Case #" + str(ct_case+1) + ": " + str(ct))

T = int(input())
for ct_case in range(0, T):
	solve()