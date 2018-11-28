def findNo(p):
	max = 0
	sum = 0
	for k in range(0,len(p)-1):
		sum = sum + p[k]
		if sum < k+1:
			if max < k + 1 - sum:
				max = k+1-sum
	return max

t = int(input())

for i in range(0,t):
	needed = 0
	p = []
	st = raw_input()
	smax = int(st[0:st.index(" ")])
	st = st[st.index(" ")+1:len(st)]
	for j in range(0,len(st)):
		p.append(int(st[j]))
		ans = "Case #" + str(i+1)+": " +str(findNo(p))
	print ans 