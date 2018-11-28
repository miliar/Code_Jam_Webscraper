T = int(input())

for i in range(1, T+1):
	smax, levels = input().split()
	smax = int(smax)

	count = 0
	answer = 0
	for j in range(0, smax+1):
		new_audience = 0
		level = int(levels[j])

		if count < j:
			new_audience = j - count

		count += new_audience+level
		answer += new_audience

	print("Case #"+str(i)+": "+str(answer))