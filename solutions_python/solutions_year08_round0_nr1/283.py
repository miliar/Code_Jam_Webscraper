# Google Codejam 2008
# Saving the Universe

def lower(x,y):
	if x>y: return y
	else: return x

for case in range(input()):
	s = input()
	engines = []
	d = {}

	for S in range(s):
		engines.append(raw_input())
	
	d = dict([i,0] for i in engines)
	min1 = 0
	ans = 0
	#if case+1==10: print engines
	
	for Q in range(input()):
		qq = raw_input()
		#if case+1==10: print qq
		d[qq] = d[qq] + 1
		min2 = reduce(lower,d.values())
		if min2>min1:
			for k in d.keys():
				d[k] = 0
			min1 = 0
			d[qq] = 1
			ans = ans + 1
			#if case+1==10: print "s"
	
	print "Case #%s: %s" % (case+1,ans)
	#if case+1==10:  print d