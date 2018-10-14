from collections import deque

def add_dict(d, num, count):
	if num not in d:
		d[num] = 0
	d[num] += count


n = int(raw_input())
for i in xrange(n):
	stalls, people = raw_input().split()
	curr = 1
	stalls = int(stalls)
	people = int(people)
	l = [(stalls,1)]
	
	while curr < people:
		d = {}
		for num, count in l:
			if (num % 2) == 0:
				add_dict(d, num/2, count)
				add_dict(d, num/2-1, count)
			else:
				add_dict(d, num/2, count*2)
		l = list(d.items())

		people -= curr
		curr = curr*2

		
	
	people -= 1

	l.sort(key = lambda x: x[0], reverse = True)
	res = l[0][0]
	if people >= l[0][1]:
		res = l[1][0]

	if res % 2 == 0:
		print 'Case #' + str(i+1) +': ' + str(res/2) + " " + str(res/2-1)
	else:
		print 'Case #' + str(i+1) +': ' + str(res/2) + " " + str(res/2)
