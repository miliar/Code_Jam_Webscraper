from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def getSubsets(s):
	possible = []
	for each in powerset(s):
		possible.append(sum(each))
	return possible	


def gimmeSmallest(my_set, V):
	all = getSubsets(my_set)

	bools = [False]*(V+1)
	#print all
	for each in all:
		if each > V:
			continue
		bools[each] = True
	#print bools
	bools = bools[1:]
	if bools.count(False) == 0:
		return -1
	return bools.index(False) + 1

#def gimmeSmallest(my_set, V):
def solve(my_set, V):
	ans = 0
	while True:
		me = gimmeSmallest(my_set,V)
	#print me
		if me == -1:
			return ans
		my_set.append(me)
		ans += 1
	return ans


f = open("C-small-attempt1.in", 'r')
#f = open("test.txt", 'r')
f2 = open("outputMoneySmall.txt", 'w')	
t = int(f.readline())
for i in xrange(t):
	s = "Case #" + str(i+1) + ": "
	
	l = f.readline().strip().split()
	v = int(l[2])
	
	l = f.readline().strip().split()
	l = map(int, l)
	ans = solve(l, v)
	#print l, v,
	##print '-----------'
	if i == t-1:
		f2.write(s+str(ans))
	else:
		f2.write(s+str(ans)+'\n')

f.close()
f2.close()
