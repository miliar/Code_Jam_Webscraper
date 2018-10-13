def solve(N, L, H, f):
	for myf in range(L, H+1):
		suc = True
		for itf in f:
			if not (itf % myf == 0 or myf % itf == 0):
				suc = False
				break
		if suc:
			return str(myf)
	return "NO"

def main():
	T = input()
	for i in range(T):
		N, L, H = [int(j) for j in raw_input().split()]
		f = [int(j) for j in raw_input().split()]
		print "Case #%d: %s" % (i+1, solve(N, L, H, f))
main()

