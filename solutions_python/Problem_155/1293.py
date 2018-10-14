T = int(input())
for i in range(1, T+1):
	D = input().split()
	Sm = int(D[0])
	S = D[1]
	k = 0
	standing = 0
	ans = 0
	while k <= Sm:
		if standing > Sm:
			break
		if standing >= k:
			standing += int(S[k])
		else:
			ans += k - standing
			standing += int(S[k]) + k - standing
		k += 1
	print("Case #{0}: {1}".format(i, ans))
