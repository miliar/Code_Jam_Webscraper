def isTidy(n):
	if len(n)==1:
		return True
	else:
		if n[0]<=n[1]:
			return isTidy(n[1:])
		else:
			return False


def findTidy(n, startWith):
	if startWith==len(n)-1:
		return n
	else:
		i = startWith
		if n[i]>n[i+1]:
			n[i] = str(int(n[i])-1)
			for j in range(i+1,len(n)):
				n[j] = "9"
		return findTidy(n, startWith+1)



t = int(raw_input())

for i in range(1,t+1):
	n = list(raw_input())
	tn = findTidy(n, 0)

	while (isTidy(tn) == False):
		tn = findTidy(tn, 0)

	j=0
	while j<len(tn):
		if tn[j] == '0':
			tn = tn[j+1:]
		if tn[j] != "0":
			break
	ans = 0
	for k in range(0, len(tn)):
		ans += int(tn[k])*(10**(len(tn)-k-1))
	
	print"Case #{}: {}".format(i, ans)
	
