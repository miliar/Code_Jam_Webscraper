# coding: cp932

def main():
	fi = open('in_large.txt')
	ncase = int(fi.readline())
	for i in range(ncase):
		P, K, L = map(int, fi.readline().split())
		ns = map(int, fi.readline().split())
		ns.sort(reverse=True)
		ns2 = []
		cnt = 0
		tmp = []
		#print 'len(ns) =', len(ns)
		#print ns
		for n in ns:
			tmp.append(n)
			cnt += 1
			if cnt == K:
				ns2.append(tmp)
				tmp = []
				cnt = 0
		ns2.append(tmp)
		#print ns2
		sum_ = 0
		for idx, ns_ in enumerate(ns2):
			sum_ += sum(ns_) * (idx+1)
		print 'Case #%d: %d' % (i+1, sum_)
	fi.close()



#import sys
#sys.setrecursionlimit(100000)
main()
