T = int(input())

def filp_pie(pies, start, end):
	pies = pies[:start] + [not pie for pie in pies[start:end]] + pies[end:]
	return(pies)

for i in range(T):
	S, K = input().split(" ")
	K = int(K)
	pies = [pie == "+" for pie in S]

	flips = 0
	for j in range(len(pies) - K + 1):
		if pies[j] == False:
			pies = filp_pie(pies, j, j+K)
			flips += 1

	# print(K, pies)
	if all(pies):
		ans = flips
	else:
		ans = "IMPOSSIBLE"
	print("Case #" + str(i+1) + ": " + str(ans))