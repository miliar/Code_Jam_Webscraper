import sys

f = sys.stdin

T = int(f.readline())
for T in xrange(1, T+1):
	N = int(f.readline())
	li = []
	for n in xrange(N):
		l = f.readline()
		a = l.rfind('1')
		li.append(a)
	N = len(li)
	v = 0
	# print T
	# import pdb; pdb.set_trace();
	while True:
		i, j = 0, 1
		finished = True
		while j < N:
			# print li
			if li[i] > i:
				if  li[j] <= i:
					t = li[i]
					li[i] = li[j]
					li[j] = t;
					v += 1
				else:
					j += 1
					while li[j] > i:
						j += 1
					v += j-i
					t = li[j]
					del li[j]
					li.insert(i, t)
					j = i + 1
				finished = False
			i += 1
			j += 1
		if finished:
			break;
	print "Case #%s: %s" % (T, v)

