import sys

fi = open('war.in.l', 'r')
T = int(fi.readline().rstrip('\n'))

for i in range(1,T+1):
		N = int(fi.readline().rstrip('\n'))
		nums = []
		for j in range(2):
				num = []
				vals = fi.readline().rstrip('\n').split(' ')
				for k in range(N):
						num.append(float(vals[k]))
				num = sorted(num)
				nums.append(num)
		s1_1 = 0
		s2_1 = 0
		s1_2 = N-1
		s2_2 = N-1
		result1 = 0
		result2 = 0
		for j in range(N):
				if nums[0][s1_1] > nums[1][s2_1]:
						s2_1 += 1
						result1 += 1
				s1_1 += 1

				if nums[0][s1_2] > nums[1][s2_2]:
						result2 += 1
				else:
						s2_2 -= 1
				s1_2 -= 1
		print 'Case #%d: %d %d' % (i,result1,result2)
