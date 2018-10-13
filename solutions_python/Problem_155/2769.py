T = int(input())

for t in range(T):
	maxS, s = input().split()
	s = [ int(c) for c in s ]

	res, standing = 0, 0

	for i in range(len(s)):
		if standing < i:

			forAdd = i - standing
			res += forAdd
			standing += forAdd

		standing += s[i]

	print ("Case #%i: %i" % (t + 1, res))
