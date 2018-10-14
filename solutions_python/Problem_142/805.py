import sys

cases = sys.stdin.readline()
cases = int(cases)


def inputing():
	global arr
	global N
	N = sys.stdin.readline()
	N = int(N)
	arr = []
	for i in range(0,N):
		arr += [sys.stdin.readline().strip()]

def work(idx):
	arr2 = [[] for i in range(N) ]
	for i in range(0,N):
		s = arr[i]
		j = 0
		while j < len(s):
			num = 0
			ch = s[j]
			while j < len(s) and s[j] == ch:
				num += 1
				j += 1
			arr2[ i ]  += [ ( ch,num ) ]

	arr0 = arr2[0]
	len0 = len(arr0)
	for i in arr2:
		if len(i) != len0:
			#print "Different len"
			return False

	num = 0
	for i in range(0,len0):
		min_num = 1<<10
		sum_num = 0
		for j in arr2:
			if j[i][0] != arr0[i][0]:
				#print "Different CHAR"
				return False # different char
			sum_num += j[i][1]
		avg = round(sum_num/N)
		r = 0
		for j in arr2:
			r += abs(avg - j[i][1])
		num += r
	print "Case #%d: %d" % (idx,num)
	return True


for i in range(cases):
	inputing()
	result = work(i+1)
	if not result:
		print "Case #%d: Fegla Won" % (i+1)


