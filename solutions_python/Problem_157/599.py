product = [[1,2,3,4],[2,-1,4,-3],[3,-4,-1,2],[4,3,-2,-1]]

def convert(x):
	return ord(x)-ord('i')+2

def mult(x,y):
	sign = 1
	if x<0:
		sign = -sign
		x = -x
	if y<0:
		sign = -sign
		y = -y

	return sign*product[x-1][y-1]

T = int(input())

for case in range(1, T+1):
	L, X = tuple([int(x) for x in input().split(' ')])
	s = input()
	s *= X

	starts = []
	ends = []

	start = convert(s[0])
	end = convert(s[-1])

	for i in range(1, L*X):
		if start == 2:
			starts.append(i)
		if end == 4:
			ends.append(L*X-i)

		start = mult(start, convert(s[i]))
		end = mult(convert(s[-i-1]), end)
		
	ans = 'NO'
	if start==-1:
		for start in starts[::-1]:
			for end in ends[::-1]:
				if end <= start:
					continue
				mid = convert(s[start])
				for i in range(start+1,end):
					mid = mult(mid, convert(s[i]))
				if mid == 3:
					ans = 'YES'
					break
			if ans == 'YES':
				break

	print('Case #', case, ': ', ans, sep='')