import fileinput
import heapq

def P1(n, k):
	if n==0:
		return (0, 0)
	if k==1:
		#print("P(%d,1)"%(n))
		return ( n>>1, (n-1)>>1 )
	tmp = P1(n, k>>1)
	#print("P_tmp(%d, %d) =" % (n, k>>1), tmp)
	if k&1:
		return P1(min(tmp), 1)
	else:
		return P1(max(tmp), 1)


def P2(n, k):
	s = ["x"*n]
	for i in range(k-1):
		s = sorted(s)
		#print(s)
		longest = s[-1][1:]
		del s[-1]
		s.append(longest[:len(longest)//2])
		s.append(longest[len(longest)//2:])
	s = sorted(s)
	#print(s)
	last_chunk = len(s[-1])
	return (last_chunk>>1, (last_chunk-1)>>1)

table_P3 = {}
def P3(n, k):
	if k==1:
		return ( n>>1, (n-1)>>1 )

	curr = 1
	h = [-n]
	#print(h)
	while (curr < k):
		top = -heapq.heappop(h)
		tmp = P3(top, 1)
		heapq.heappush(h, -(top>>1))
		heapq.heappush(h, -((top-1)>>1))
		curr += 1
		#print(sorted(h))

	#print(sorted(h))
	return P3(-heapq.heappop(h), 1)


counter = 0
for line in fileinput.input():
	if not fileinput.isfirstline():
		n, k = map(int, line.split(' '))
		sol = P3(n, k)
		counter += 1
		print("Case #%d: %d %d" % (counter, sol[0], sol[1]))

