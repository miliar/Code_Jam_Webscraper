
file = "./C-large.in"
file_ans = "./stall.out"

def solve_quick(n, k):
	num = 1
	a = 1   # a - how many splited nicely, b - how many are smaller by 1
	b = 0
	while True:
		#print "n=%d, num=%d, k=%d, a,b=%d,%d" % (n, num, k, a, b)
		
		if k <= num:
			#print "end, k=", k
			if k <= a:
				res = n
			else:
				res = n-1
			break

		else:
			k -= num
			num *= 2
			
			if n % 2 == 1:
				a = 2*a + b
			else:
				b = a + 2*b

			n /= 2

	#print "res", res
	return ( (res)/2, (res-1)/2)

def solve(n, k):
	t = [n]
	pos = 0
	for i in range(k):
		curr = t[pos]
		if curr == 1:
			continue
		t.append(curr / 2)
		if curr >= 2:
			t.append((curr-1) / 2)
		t.sort()
		t.reverse()
		pos += 1
	print pos, t[pos], t


with open(file, "r") as f:
	with open(file_ans, "w") as fout:

		T = int(f.readline())
		for t in range(T):
			n, k = map(int, f.readline().split())
			sol = solve_quick(n,k)
			fout.write("Case #%d: %d %d\n" % (t+1, sol[0], sol[1]))
				


#print solve_quick(500, 244)
#solve(500, 244)
#solve(1005, 1000)

# for i in range(1,12):
# 	print i, solve_quick(11, i), "\n"