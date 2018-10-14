T = int(raw_input())
for i in range(T):
	no = raw_input()
	for j in range(len(no) - 1):
		if no[j] > no[j + 1]:
			if no[j] == '1':
				no = '9' * (len(no) - 1)
				break
			else:
				if no[0 :j + 1] == no[j] * (j + 1):
					no = str(int(no[j]) - 1) + '9' * (len(no) - 1)
				else:
					no = no[0 : j] + str(int(no[j]) - 1) + '9' * (len(no) - 1 - j)
					break
	print 'Case #' + str(i + 1) + ':' + ' ' + str(int(no))