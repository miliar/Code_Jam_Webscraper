from math import pi

def outer_area(r, h):
	return 2*r*pi*h
	
def top_area(r):
	return r*r*pi

f = open('A-large.in', 'r')
g = open('output.txt', 'w')

t = int(f.readline())

for case in xrange(t):
	n,k = map(int, f.readline().split())
	
	pancakes = []
	
	for x in xrange(n):
		r,h = map(int, f.readline().split())
		outer = outer_area(r,h)
		top = top_area(r)
		pancakes.append((outer, top))
		
	pancakes.sort(reverse = True)
	
	outers = sum(pancake[0] for pancake in pancakes[:k])
	top = max(pancakes[:k], key = lambda pancake: pancake[1])[1]
	area = outers+top
	lowest_included_outer = pancakes[k-1][0]
	best_exchange = 0.0
	
	for i in xrange(k, n):
		loss = lowest_included_outer - pancakes[i][0]
		increase = pancakes[i][1] - top

		best_exchange = max(best_exchange, increase-loss)
		
	endl = '' if case == t-1 else '\n'
	g.write('Case #' + str(case+1) + ': ' + str(area + best_exchange) + endl)