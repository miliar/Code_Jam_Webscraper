cases = int(raw_input())
for c in range(1, cases+1):
	num = "0" + raw_input()
	inc = 0
	dec = -1
	for i in range(len(num)-1):
		if num[i] > num[i+1]:
			dec = i
			break
		if num[i] < num[i+1]:
			inc = i
	if dec != -1:
		pre = num[:inc+1]
		mid = str(int(num[inc + 1]) - 1)
		end = '9' * (len(num) - (inc + 2))
		num = pre + mid + end
	print "Case #" + str(c) + ": " + str(int(num))
