

t = int(raw_input())
for p in range(t):
	sum = 0
	input = raw_input().split(' ')
	r = int(input[0])
	k = int(input[1])
	n = int(input[2])
	list = raw_input().split(' ')
	i = 0
	while i < r:
		complete = False
		localSum = 0
		l = 0
		auxList = []
		while (l<len(list)) and (localSum+int(list[l])) <= k:
			localSum = localSum + int(list[l])
			auxList = auxList + [list[l]]
			l = l + 1
		list = list[l:] + auxList
		sum = sum + localSum
		i = i + 1
	print 'Case #%d: %d' %(p+1,sum)

