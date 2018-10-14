from math import pi

def compare(x,y):
	return y[1]*y[0] - x[1]*x[0]

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

cases = int(input())

for casenum in range(1,cases+1):
	N, K = ( int(x) for x in input().split() )

	pancakes = []
	radii = set()
	for i in range(N):
		pancakes.append([int(x) for x in input().split()])
		radii.add(pancakes[-1][0])

	pancakes.sort(key=cmp_to_key(compare))

	res = 0

	for i in range(N):
		c = 1
		radius = pancakes[i][0]
		surface = radius*radius + 2*radius*pancakes[i][1]
		if K > 1:
			for j in range(N):
				if i == j:
					continue
				pancake = pancakes[j]
				if pancake[0] > radius:
					continue
				surface += 2*pancake[0]*pancake[1]
				c += 1
				if c == K:
					break
		if c == K and surface > res:
			res = surface

	print("Case #", casenum, ": ", res*pi, sep="")

