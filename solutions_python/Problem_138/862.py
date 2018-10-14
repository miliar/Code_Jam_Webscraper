def war(a, b, n):
	t = 0
	for i in range(n):
		flag = False
		j = 0
		while j < len(b) and not flag:
			if b[j] > a[i]:
				t += 1
				b.pop(j)
				flag = True

			j += 1

		if not flag:
			b = b[1:]
		
	return n-t

def deceitful(A, B, n):
	a = [x for x in A]
	b = [x for x in B]
	t = 0

	for i in range(n):
		if a[i] > b[0]:
			b.pop(0)
			t += 1
		else:
			b = b[:-1]

	return t

def main():
	T = int(raw_input())

	for t in range(1, T+1):
		N = int(raw_input())
		Naomi = sorted([float(x) for x in raw_input().split(' ')])
		ken = sorted([float(x) for x in raw_input().split(' ')])

		print "Case #{0}: {1} {2}".format(t, deceitful(Naomi, ken, N), war(Naomi, ken, N))

main()