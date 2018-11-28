import sys
import math

sys.stdout = open('out', 'w')
with open(sys.argv[1], 'r') as f:
	l = f.readline().split(' ')
	for p in range(int(l[0])):
		l = f.readline().split(' ')
		num = list(l[0])
		del num[len(num) - 1]
		num = [int(x) for x in num]
		for i in range(len(num)-1,0,-1):
			if num[i-1] > num[i]:
				num[i-1] -= 1
				for j in range(i,len(num),1):
					num[j] = 9
		for i in range(len(num)):
			if num[i] == 0:
				del num[i]
			else:
				break
		num = [str(x) for x in num]
		num = ''.join(num)
		print "Case #" + str(p + 1) + ":", num

