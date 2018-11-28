import math as m

with open('input.txt', 'r') as inFile, open('output.txt', 'w') as outFile:
	
	T = int(inFile.readline())
	for c in range (T):
		A, B = list(map(int, inFile.readline().strip().split()))
		a = round(m.pow(A, 0.5) - 1)
		b = round(m.pow(B, 0.5) + 1)
		print(A, a, B, b)
		count = 0
		for i in range (a, b + 1):
			q = 0
			s = str(i)
			l = len(s)
			for j in range ((l + 1)// 2):

				if s[j] != s[l-j - 1]:
					q = 1
					break
			if q : continue
			s = str(i * i)
			l = len(s)
			for j in range (l // 2):
				if (i * i > B) or (i * i < A) or s[j] != s[l-j - 1]:
					q = 1
					break
			print (i*i, B, q, i)
			if not q and (i * i <= B) and (i * i >= A): 
				count += 1


		outFile.write('Case #{0}: {1}\n'.format(c + 1, count))
