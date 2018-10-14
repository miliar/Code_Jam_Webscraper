cases = int(input())

for c in range(1,cases+1):
	raw = input().split()
	pan = list(raw[0])
	L = int(raw[1])

	count = 0

	for i in range(len(pan)-L+1):
		if pan[i] == '-':
			count += 1
			for j in range(i, i+L):
				pan[j] = '+' if pan[j] == '-' else '-'

	success = (pan[-L:] == ["+"]*L)

	print("Case #", c, ": ", count if success else "IMPOSSIBLE", sep="")

