def f(n):
	a = list(str(n))
	N = len(a)
	for i in range(N-1):
		if a[i] > a[i+1]:
			return(f( (int(''.join(a[:i+1])))*10**(N-i-1)-1 ))
	return n

with open("in.bin","r") as fin:
	w = fin.read().split('\n')
	T = w[0]
	val = w[1:]
	for i in range(1,len(val)):
		print("Case #%d: %d" % (i, f(int(val[i-1]))))
