"""
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input())
	answ = 0
	for k in reversed(range(n+1)):
		l = map(int, str(k))
		sw = all(l[j] <= l[j+1] for j in xrange(len(l)-1))
		if sw:
			break

	print "Case #{}: {}".format(i, k)
"""

t = int(raw_input())  # read a line with a single integer
for k in xrange(1, t + 1):
	n = int(raw_input())
	num = map(int, str(n))
	for i in reversed(range(1,len(num))):
		if num[i-1] > num[i]:
			num[i-1] -= 1
			for j in range(i,len(num)):
				num[j] = 9


	print "Case #{}: {}".format(k, int(''.join([str(n) for n in num])))

"""
111111111111111110 ->  

132 ->  

132132 -> 132129 -> 131999 -> 129999
  
23432 -> 23429
23399
"""