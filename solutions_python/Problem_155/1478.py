
t = int(input())
cnt = 1

while (t):
	x, y = input().split()
	x = int(x)

	sum, guest = 0, 0
	for i in range(x+1):
		if int(y[i]) is 0:
			continue

		if sum < i:
			guest += i - sum
			sum += i - sum

		sum += int(y[i])

	print("Case #"+ str(cnt) + ": "+ str(guest))

	t -= 1
	cnt += 1