with open('C-small-attempt0.in', 'r') as inFile, open('c.out', 'w') as outFile:
	n = int(inFile.readline()) + 1
	for i in range (1, n) :
		ans = 0
		(a, b) = list(map(int, inFile.readline().strip().split()))
		for j in range (a, b + 1) :
			j_str = str(j)
			j_len = len(j_str)
			if j_len < 2 : continue
			for k in range (1, j_len) :
 				j_new = j_str[k:] + j_str[:k]
 				if (a <= int(j_new) <= b) and (j_str != j_new) : ans += 1
		ans = int(ans / 2) 
		outFile.write("Case #" + str(i) + ": " + str(ans) + "\n")
