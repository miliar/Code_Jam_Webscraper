#!/usr/bin/python

T = int(raw_input())
for t in range(T):
	R, k, n = tuple([int(item) for item in raw_input().split()])
	l = [int(item) for item in raw_input().split()]
	capacity = [0]*n
	money = [0]*n
	for i in range(n):
		cur = k - l[i]		
		capacity[i] = 1
		j = (i + 1)%n
		while (cur - l[j] >= 0) and (j != i):
			capacity[i] += 1
			cur -= l[j]
			j = (j + 1)%n
		money[i] = k - cur

	was = [False]*n

	i = 0
	while not was[i]:
		was[i] = True
		i = (i + capacity[i])%n
	cyclic = i
	cycle_money = money[i]
	cycle_length = 1
	j = (cyclic + capacity[i])%n
	while j != cyclic:
		cycle_money += money[j]
		cycle_length += 1
		j = (j + capacity[j])%n

	# Solution
	ans = 0
	i = 0
	while R > 0:
		if (i == cyclic) and (R > cycle_length):
			ans += (R/cycle_length) * cycle_money
			R %= cycle_length
		else:
			ans += money[i]
			R -= 1
			i = (i + capacity[i])%n

	print "Case #" + str(t + 1) + ": " + str(ans)