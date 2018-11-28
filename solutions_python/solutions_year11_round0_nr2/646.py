#!/usr/bin/python

def build_combination_dict(lis):
	
	dc = {}
	for st in lis:
		dc[st[:-1]] = st[-1]
		dc[st[:-1][::-1]] = st[-1]
	return dc

def build_opp_set(lis):
	
	l = []
	for x in lis:
		l.append(x)
		l.append(x[::-1])
	return set(l)

def turn(elem_list, letter, comb_dict, opp_set):
	
	# Check for combination
	lis = []
	if len(elem_list) > 0:
		st = '%s%s' % (letter, elem_list[-1])
		if comb_dict.get(st, None):
			return elem_list[:-1] + [comb_dict.get(st, None)]
		if comb_dict.get(st[::-1], None):
			return elem_list[:-1] + [comb_dict.get(st[::-1], None)]
		
	# Check for opposition
	for x in elem_list:
		st = '%s%s' % (letter, x)
		if st in opp_set or st[::-1] in opp_set:
			return []
			
	return elem_list + [letter]

def case(invocation, comb_dict, opp_set):
	
	el_list = []
	for x in xrange(0, len(invocation)):
		el_list = turn(el_list, invocation[x], comb_dict, opp_set)
	return str(el_list).replace("'", '')

def get_input():
	
	fil = open('magicka.in')
	lines = fil.readlines()
	
	ans = []
	for lin in lines[1:]:
		spl = lin.replace('\n', '').split(' ')
		comb_list = []
		cnt = 0
		for x in xrange(1, int(spl[0])+1):
			cnt = x
			comb_list.append(spl[cnt])
		cnt = cnt + 1
		opp_list = []
		#print cnt, spl, comb_list
		for x in xrange(cnt+1, cnt+int(spl[cnt])+1):
			cnt = x
			opp_list.append(spl[cnt])
		invok = spl[-1]
		ans.append( (comb_list, opp_list, invok) )
	#print ans
	#print ans
	return ans

def main():
	
	#base_elem_list = set(['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'])
	out = open('magicka.out', 'w')
	i = 1
	for (comb_list, opp_list, invoks) in get_input():
		comb_dict = build_combination_dict(comb_list)
		#print comb_dict
		opp_set = build_opp_set(opp_list)
		#print opp_set
		lis = [x for x in invoks]
		st = "Case #%s: %s" % (i, case(lis, comb_dict, opp_set))
		print st
		print>>out, st
		i = i + 1
	out.close()

if __name__ == "__main__":
	
	main()
