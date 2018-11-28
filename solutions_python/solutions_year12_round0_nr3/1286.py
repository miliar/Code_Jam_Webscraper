#!/usr/bin/python
from collections import deque

def main():
	fin = open('C-small-attempt0.in', 'r')
	fout = open('C.out','w')
	T = long(fin.readline())
	d = {}
	for t in range(1,T+1):
		[mn, mx] = map(long, fin.readline().split())
		count =0;
		ss = set()
		for it in range(mn, mx+1):
			s = ''.join(str(it))
			ss.add(s)
			l = cy(list(str(it)))
			for i in l:
				stt = long(''.join(i))
				#print str(mn) + ' -- ' + str(it) + '---->' + str(stt) + ' -- ' + str(mx)
				if (stt >= mn and stt <= mx and str(stt) not in ss):
					#ss.add(str(stt))
					count+=1

		fout.write("Case #" + str(t) + ": " +str(count) +"\n")

def cy(lis):
	re = []
	q = deque(lis)
	st1 = ''.join(lis)
	s = set(st1)
	for i in range(len(lis)):
		q.rotate(1)
		st = ''.join(list(q))
		if st == st1:
			break
		if st not in s:
			re.append(list(q))
			s.add(st)
	return re
	
if __name__ == '__main__':
	main()

