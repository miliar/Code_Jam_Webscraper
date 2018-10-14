import sys

def srt(x):
	assert x >= 0
	min=0
	sup=x+1
	while min+1<sup:
		mid=(min+sup)/2
		if mid*mid<=x:
			min=mid
		else:
			sup=mid
	assert min*min <= x
	assert (min+1)*(min+1) > x
	return min

def ispall(x):
	y=str(x)
	for i in range(len(y)/2):
		if y[i] != y[len(y)-1-i]:
			return False
	return True

def solve(low,upp):
	ll = srt(low)
	uu = srt(upp)+1
	count = 0
	for x in range(ll,uu+1):
		if ispall(x):
			y = x*x
			if ispall(y) and low <= y <= upp:
				count += 1
	return count

if __name__=='__main__':
	r = int(sys.stdin.readline())
	for k in range(r):
		l = sys.stdin.readline()
		ll=l.split(' ')
		assert len(ll)==2
		low = int(ll[0])
		upp = int(ll[1])
		ans = solve(low,upp)
		print "Case #"+str(k+1)+": "+str(ans)


