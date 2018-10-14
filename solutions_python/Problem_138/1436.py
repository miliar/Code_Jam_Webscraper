

from sys import stdin
import bisect


def readline(): return stdin.readline().strip('\n')
def readint(): return int(readline())

def war(naomi, Ken):
	pts = 0
	ken = Ken[:]
	for x in range(len(naomi)):
		i = bisect.bisect_right(ken, naomi[x])
		if i >= len(ken):
			pts += 1
			ken.pop()
		else:
			ken.pop(i)

	return pts


def deceitful_war(naomi, Ken):
	pts = 0
	naomi = naomi[:]
	ken = Ken[:]
	Len = len(naomi)
	for x in range(Len):
		if naomi[-1] > ken[-1]:
			pts += 1
			naomi.pop()
			ken.pop()
		else:
			naomi.pop(0)
			ken.pop()

	return pts



T = readint()

for t in range(1, T+1):
	N = readint()
	naomi = sorted([float(x) for x in readline().split(' ')])
	ken = sorted([float(x) for x in readline().split(' ')])
	
	#print N, naomi, ken

	print 'Case #' + str(t) + ': ' + str(deceitful_war(naomi, ken)) + ' ' + str(war(naomi, ken))

