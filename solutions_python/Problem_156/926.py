import numpy


# precompute times : t[P, a] is the optimal time to eat P pancakes with a actions
Pmax = 10
amax = 10#int(numpy.sqrt(Pmax)+3)
tArray = numpy.zeros((Pmax, amax))
for P in range(Pmax):
	for a in range(amax):
		if a == 0:
			tArray[P, a] = P
		else:
			tArray[P, a] = tArray[P, a-1]
		for i in range(P+1):
			for b in range(a):
				tArray[P, a] = min(tArray[P, a], max(tArray[i, b],tArray[P-i, a-1-b]))
aArray = numpy.zeros((Pmax, Pmax))
for P in range(Pmax):
	for t in range(1, Pmax):
		aArray[P, t] = numpy.min(numpy.nonzero(tArray[P,:]<=t))
#print tArray
#print aArray

f = open('B-small-attempt0.in', 'r')

T = int(f.readline())
for n in range(T):
	D = int(f.readline())
	P_i_strings = f.readline().split(' ')
	P_i = numpy.zeros(D)
	for i in range(D):
		P_i[i] = int(P_i_strings[i])
	actionsToDo = numpy.zeros(max(P_i)+1)
	actionsToDo[0] = max(P_i)+1
	for i in range(1, int(max(P_i))):
		for j in range(D):
			actionsToDo[i] = actionsToDo[i] + aArray[P_i[j], i]
	#print actionsToDo
	#print range(int(max(P_i)+1))
	timeToEat = min(actionsToDo + range(int(max(P_i)+1)))
	print 'Case #' + str(n + 1) + ': ' + str(int(timeToEat))
