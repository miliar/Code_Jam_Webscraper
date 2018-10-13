in_file = open("input.txt", "r")
out_file = open("output.txt", "w")


def doIt(n, k):
	a = []
	for i in range(n):
		a.append(0)
	lst = -1
	while k > 0:
		k -= 1
		l = -1
		r = -1
		id = -1
		i = -1
		j = 0
		while i < n:
			while j < n and a[j] == 0:
				j += 1
			mid = int((i + j) / 2)
			nl = mid - i + 1
			nr = j - mid - 1
			if min(l, r) < min(nl, nr) or (min(l, r) == min(nl, nr) and max(l, r) < max(nl, nr)):
				l = nl
				r = nr
				id = mid
			i = j
			j += 1
		a[id] = 1
		lst = id
	l = 0
	i = lst - 1
	while i >= 0 and a[i] == 0:
		i -= 1
		l += 1
	r = 0
	i = lst + 1
	while i < n and a[i] == 0:
		i += 1
		r += 1
	return (max(l, r), min(l, r))



def solve():
	n = int(in_file.readline())
	for t in range(1, n + 1):
		out_file.write("Case #" + str(t) + ": ")
		(n, k) = in_file.readline().split()
		n = int(n)
		k = int(k)
		ans = doIt(n, k)
		out_file.write(str(ans[0]) + " " + str(ans[1]) + "\n")
		

solve()

in_file.close()
out_file.close()
