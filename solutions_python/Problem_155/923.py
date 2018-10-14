import sys

t = int(input())
k = 1
while (t>0):
	t -= 1
	sys.stdout.write('Case #'+str(k)+': ')
	k += 1

	maxi, s = raw_input().split()
	maxi = int(maxi)
	ans = 0
	p = 0
	count = 0
	while (maxi >= 0):
		if (p<=count):
#			print maxi, p
			count += int(s[p])
			p += 1
			maxi -= 1
		else:
#			print s[p], count, ans
			ans += p-count
			count = p
	print ans
