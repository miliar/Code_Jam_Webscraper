test = int(input())

for t0 in range(test):
	q = input().strip()
	while q!=''.join(sorted(q)):
		q=str(int(q)-1)
	print("Case #"+str(t0+1)+": "+q)