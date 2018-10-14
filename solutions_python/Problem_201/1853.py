if __name__ == '__main__':

	caseNum = int(input())
	

	for i in range(caseNum):
		
		n, k = [int(s) for s in input().split(" ")]
		t = 1
		while t <= k:
			t = t*2

		tree = [0 for s in range(t)]
		tree[0] = k
		tree[1] = n
		ht = int(t/2)

		for j in range(1,ht):
			if tree[j]%2 == 0:
				tree[2*j] = tree[j]/2 - 1
				tree[2*j+1] = tree[j]/2
			else:
				tree[2*j] = (tree[j]-1)/2
				tree[2*j+1] = tree[2*j]

		lastRow = tree[ht:t]
		lastRow = sorted(lastRow,reverse = True)
		space = lastRow[k-ht]
		if space%2 == 0:
			ls = int(space/2 - 1)
			rs = int(space/2)
		else:
			ls = int((space-1)/2)
			rs = ls

		print("Case #{}: {} {}".format(i+1,max(ls,rs),min(ls,rs)))



