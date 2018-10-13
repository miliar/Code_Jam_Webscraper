import heapq
import math
f = open("input.in","r")
fout = open("output.out","w")
tt = int(f.readline())
case = 0


def find(a):
	no = abs(a[0])
	x = heapq.heappop(a)
	if (abs(x)<2) : return no
	x1 = x/2
	x2 = x-x1
	heapq.heappush(a,x1)
	heapq.heappush(a,x2)
	yes = find(a)+1
	return min(yes,no)

def check(a,d):
	i = 0
	while i<d:
		y = i
		x = d-i
		for j in a:
			if j>x:
				y -= int(math.ceil(float(j)/x))-1
				if (y<0): break
			else: 
				break
		if (y>=0): return True
		i+=1
	return False


while tt>0:
	tt-=1
	n = int(f.readline())
	a = map(lambda x: int(x),f.readline().split(' '))
	a.sort(reverse=True)
	
	l = 0
	r = a[0]+1
	# print l,r
	while l<r:
		mid = (l+r)/2
		if (check(a,mid)):
			r = mid
		else:
			l = mid+1
	ans = l

	case+=1
	# print ans
	fout.write("Case #"+str(case)+": "+str(ans)+"\n")
	



