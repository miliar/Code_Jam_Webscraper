import sys

def get_min(cur):
		p = ''
		result = []
		min = []
		c = 0
		for ch in cur:
				if ch == p:
						c += 1
				else:
						if p != '':
								min.append(p)
								result.append(c)
						p = ch
						c = 1
		min.append(ch)
		result.append(c)
		#print min
		return min,result

def median_sum(strs, j):
		nums = []
		for ct in strs:
				nums.append(ct[j])
		nums = sorted(nums)
		mid = (len(nums)-1)/2
		result = 0
		for num in nums:
				result += abs(nums[mid] - num)
		return result

fi = open('rt.in','r')
T = int(fi.readline().strip())
for i in range(1,T+1):
		N = int(fi.readline().strip())
		strs = []
		min = ''
		valid = False
		diff = 0
		for j in range(N):
				cur = fi.readline().strip()
				if valid == True:
						continue
				cur_min,cur_count = get_min(cur)
				if min == '':
						min = cur_min
				elif cur_min != min:
						print "Case #%d: Fegla Won" % i
						valid = True
						continue
				strs.append(cur_count)
				diff += len(cur) - len(min)
		if valid == True:
				continue
		
		#print strs
		#print min
		result = 0
		for j in range(len(min)):
				result += median_sum(strs, j)
		print "Case #%d: %d" % (i,result)
