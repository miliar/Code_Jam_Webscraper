def comb(a):
	return [ c-b for b in a for c in a if b < c]

def mcd(n, m):
	if m == 0: return n
	return mcd(m, n%m)

if __name__ == '__main__':
	fin = open('b.in')
	fout = open('b.out', 'w')
	cases = int(fin.readline())
	for c in range(cases):
		input = map(int, fin.readline().split(' '))
		n = input[0]
		a = input[1:]
		a.sort()
		T = reduce(mcd, comb(a))
		fout.write("Case #%d: %d\n"%(c+1, -a[0]%T if T > 1 else 0))
