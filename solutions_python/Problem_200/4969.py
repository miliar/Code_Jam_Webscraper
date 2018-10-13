'''def solve(n):
	if n>=1 and n<=9 :
		return n
	else :
		m = str(n)
		i = 1
		tidy = False
		while n > 0:
			while i < len(m):
				if int(m[i]) >= int(m[i-1]):
					i += 1
					tidy = True
			if tidy:
				return n
			else:
				n -= 1
				continue
				
	'''

def solve(n):
	tidy = False

	if n>0 and n<10:
		tidy = True
	else:
		x = 0
		for each in str(n):
			each = int(each)
			if ( each >= x):
				tidy = True
				x = each
			else:
				tidy = False
				break
	if tidy:
		return n
	else:
		return solve(n-1)




t = int(input().strip())

for case in range(1, t+1):
	n = int(input())
	print("Case #{}: {}".format(case, solve(n)))