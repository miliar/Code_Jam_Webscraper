from sys import stdin

def solve(e):
	for i in range(1,len(e)):
		if e[i-1] > e[i]:
			e[i-1] -= 1
			e[i:] = [9]*(len(e)-i)
			return (e,True)	
	return (e,False)

if __name__ == '__main__':
	n = int(stdin.readline())
	i = 1
	for _ in range(n):
		e = [int(x) for x in stdin.readline()[:-1]]

		e, l = solve(e)
		while (l):				
			e, l = solve(e)

		cc = 0
		for x in e:
			if x == 0:
				cc += 1
			else:
				break
		e = e[cc:]
	
		
		out = "".join(str(x) for x in e)
		print("Case #{}: {}".format(i,out))
		i+=1

