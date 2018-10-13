with open('B-large.in', 'r') as inFile, open('B-large.out', 'w') as outFile:
	t = int(inFile.readline()) + 1
	ans = 0	
	for i in range (1, t) :
		ans = 0
		arr = list(map(int, inFile.readline().strip().split()))
		n = arr.pop(0)
		s = arr.pop(0)
		p = arr.pop(0)
		if not p :
			outFile.write("Case #" + str(i) + ": " + str(n) + "\n")
			continue
		arr.sort()
		arr.reverse()
		k = (p - 1) * 3
		while len(arr) and (arr[0] > k) :
			ans += 1 
			arr.pop(0)
		k -= 1
		for j in range (s) :
			if not arr : break
			if not arr[0] : break
			if arr[0] >= k : ans += 1
			arr.pop(0)
		outFile.write("Case #" + str(i) + ": " + str(ans) + "\n")