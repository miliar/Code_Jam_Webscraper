f = open('A-large.in', 'r')
ans = open('result.txt', 'w')

T = int(f.readline().strip())

for t in xrange(0, T):
	line = f.readline().strip()

	parts = [x for x in line.split(" ")]

	SMAX = int(parts[0].strip())

	result = [0] * len(parts[1])

	result[0] = int(parts[1][0])

	invited = 0

	for i in xrange(1, len(parts[1])):
		S_i = int(parts[1][i])

		if S_i > 0 and result[i - 1] < i:
			invite = i - result[i - 1]
			invited += invite

			result[i] = result[i - 1] + S_i + invite
		else:
			result[i] = result[i - 1] + S_i
			

	ans.write("Case #"+str(t+1)+": " +str(invited)+ '\n')