import itertools
import sys

#itertools.permutations([1,2,3])

def check(li):
	a = 0
	for i in range(1, len(li)):
		if a == 0:
			if li[i] < li[i-1]:
				a = 1
		elif a == 1:
			if li[i] > li[i-1]:
				a = 2
	return False if a == 2 else True

def com(a, b):
	t = 0
	#print b
	for i in range(len(a)):
		for j in range(i, len(a)):
			if b[j] == a[i]:
				m = j
		for j in range(m, i, -1):
			#print j, m, b[j], b[j-1]
			b[j], b[j-1] = b[j-1], b[j]
			t += 1
		#print a, b
	return t

sno = int(sys.argv[1])
eno = int(sys.argv[2])

ecase = int(sys.stdin.readline().strip())
for ecount in range(1, ecase+1):
	en = int(sys.stdin.readline().strip())
	nums = sys.stdin.readline().split()
	nums = [int(x) for x in nums]
	#print nums
	ans = 99999999
	print >>sys.stderr, ecount
	if sno <= ecount and ecount <= eno:
		for p in itertools.permutations(nums):
			pl = list(p)
			if check(pl):
				#print pl
				t = com(nums, pl)
				if t < ans:
					ans = t
					#print pl
		
		print "Case #%d: %d" % (ecount, ans)
