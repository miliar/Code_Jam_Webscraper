import sys

t=int(input())
k = 1
while t>0:
	t-=1
	sys.stdout.write('Case #'+str(k)+': ')
	k += 1

	n = int(input())
	arr = [int(a) for a in raw_input().split()]

	ans1 = 0
	ans2 = 0
	for i in xrange(n-1):
		if (arr[i+1]<arr[i]):
			ans1 += arr[i]-arr[i+1]

	maxdiff = 0
	for i in xrange(n-1):
		if (arr[i]-arr[i+1]>maxdiff):
			maxdiff = arr[i]-arr[i+1]

	for i in xrange(n-1):
		l = arr[i]-maxdiff
		if l<0:
			ans2 += arr[i]
		else:
			ans2 += maxdiff

	print ans1, ans2