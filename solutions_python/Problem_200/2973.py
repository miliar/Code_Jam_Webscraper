T = int(raw_input())
for i in range(T):
	no = raw_input()
	for j in range(len(no) - 1):
		if no[j] > no[j + 1]:
			no = no[0 : j] + str(int(no[j]) - 1) + '9' * (len(no) - 1 - j)
			for k in range(j, 0, -1):
				if no[k] < no[k - 1]:
					no = no[0 : k - 1] + str(int(no[k - 1]) - 1) + '9' * (len(no) - k)
	print 'Case #' + str(i + 1) + ':' + ' ' + str(int(no))