
t = int(input())

for case in range(1, t + 1):
	count = 0

	s, k = [s for s in input().split(" ")]
	k = int(k)

	#print(s, k)
	for i in range(len(s) - k + 1):
		if s[i] == "-":
			count += 1
			flip = ""
			for j in range(k):
				flip += s[i + j] == "+" and "-" or "+"
			s = s[:i] + flip + s[i+k:]
			#print("\t", s)

	if "-" not in s:
		print("Case #%d: %d" % (case, count))
	else:
		print("Case #%d: IMPOSSIBLE" % case)