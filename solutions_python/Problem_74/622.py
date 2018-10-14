#!/usr/bin/python

def build_actions(instrs):
	
	locs = [1, 1]
	acts = []
	for (id, loc) in instrs:
		
		#acts.append(('M', id, loc - locs[id]))
		locs[id] = loc
		acts.append(('P', id, loc))
		
	return acts

def get_next_dest(acts, id):
	
	ar = [x for x in acts if x[0] == 'P' and x[1] == id]
	if len(ar) > 0:
		return ar[0][2]
	else:
		return -1

def get_next_press(acts):
	
	ar = [x for x in acts if x[0] == 'P']
	if len(ar) > 0:
		return ar[0][1]
	else:
		return -1

def compress_actions(acr):
	
	time = 0
	locs = [1,1]
	acts = acr
	nexts = [get_next_dest(acts, 0), get_next_dest(acts, 1)]
	nextp = get_next_press(acts)

	dic = ['O', 'B']
	while nextp != -1:
		
		print time, locs, nexts, nextp
		dif = nexts[nextp] - locs[nextp]
		time = time + abs(dif) + 1
		locs[nextp] = nexts[nextp]
		print '%s moved to %s and pushed' % (dic[nextp], locs[nextp])
		
		if nexts[1-nextp] != -1:
			
			sgn = -1
			if locs[1-nextp] < nexts[1-nextp]:
				sgn = +1
			elif locs[1-nextp] == nexts[1-nextp]:
				sgn = 0
			locs[1-nextp] = locs[1-nextp] + (sgn) * abs(dif+1)
			print '%s moved to %s' % (dic[1-nextp], locs[1-nextp])
		
		acts = acts[1:]
		nexts = [get_next_dest(acts, 0), get_next_dest(acts, 1)]
		nextp = get_next_press(acts)
		
	return time

def sgn(x):
	
	if x < 0:
		return -1
	elif x == 0:
		return 0
	else:
		return 1

def compress_actions2(acr):
	
	time = 0
	locs = [1,1]
	acts = acr
	nexts = [get_next_dest(acts, 0), get_next_dest(acts, 1)]
	nextp = get_next_press(acts)

	dic = ['O', 'B']
	while nextp != -1:
		
		#print time, locs, nexts, nextp
		time = time + 1
		sgns = map(sgn, map(lambda (a,b):a-b, zip(nexts, locs)))
		if sgns[nextp] == 0:
			acts = acts[1:]
			nextp = get_next_press(acts)
			nexts = [get_next_dest(acts, 0), get_next_dest(acts, 1)]
		
		locs = map(lambda (a,b):a+b, zip(sgns, locs))

	return time

def get_input():
	
	fil = open('bottrust.in')
	lines = fil.readlines()
	
	ans = []
	dic = {'O':0,'B':1}
	for lin in lines[1:]:
		spl = lin.replace('\n', '').split(' ')
		lis = spl[1:]
		xls = []
		for x in xrange(0, len(lis)):
			if x % 2 == 0:
				xls.append((dic[lis[x]], int(lis[x+1])))
		ans.append(xls)
	#print ans
	return ans

def main():
	
	inp = get_input()
	i = 1
	out = open('bottrust.out', 'w')
	for instrs in inp:
		acts = build_actions(instrs)
		#print acts
		time = compress_actions2(acts)
		st = "Case #%s: %s" % (i, time)
		print st
		print>>out, st
		i = i + 1
	out.close()

if __name__ == "__main__":
	
	main()
