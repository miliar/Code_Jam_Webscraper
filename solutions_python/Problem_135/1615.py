import fileinput as f

def eval_case(vol1, vol2, arr1, arr2):
	set1 = arr1[vol1-1] 
	set2 = arr2[vol2-1]
	ans  = set1 & set2

	if not ans:
		return "Volunteer cheated!"
	elif len(ans) is 1:
		return str(ans.pop())
	else:
		return "Bad magician!"

def parse_input():

	cases  = 0
	v1, v2 = 0, 0
	a1     = []
	a2     = []
	case_n = 1

	for x in f.input():
		if f.isfirstline():
			cases = int(x)
		if case_n > cases:
			break
		else:
			j = (f.lineno()-1) % 10
			if j is 1:
				if v1:
					print "Case #%s: %s" % (case_n, eval_case(v1,v2,a1,a2))
					case_n += 1
				v1 = int(x)
			elif j is 6:
				v2 = int(x)
			elif j > 1 and j < 6: # first arrangement
				if j is 2:
					a1 = []  #clear
					a2 = []  #clear
				a1.append(set([int(n) for n in x.split()]))
			elif j is 0 or (j > 6 and j < 10):
				a2.append(set([int(n) for n in x.split()]))
	print "Case #%s: %s" % (case_n, eval_case(v1,v2,a1,a2))

parse_input()
