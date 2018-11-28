def get_permutations(a, b):
	retset = set()

	for i in xrange(a,b+1,1):
		istr = str(i)
		for k in range(len(istr)):
			kstr = istr[k:] + istr[:k]
			kstri = int(kstr)
			istri = int(istr)
			if kstri <= b and kstri >= a:
				retset.add(kstri)
	return retset

def fuzzy_match(a,b):
	for i in range(len(str(a))):
		astr = a[i:] + a[:i]
		if b == astr:
			return True
	return False


def solve(line):
	a_set = get_permutations(int(line[0]), int(line[1]) )
	count = 0
	for a in a_set:
		for b in a_set:
			if b>a and fuzzy_match(str(a),str(b)):
				count += 1
	return str(count)

def main():
	t = int(input())
	case_num = 0

	while case_num < t:
		case_num += 1
		line = [str(x) for x in raw_input().split()]
		print "Case #%d: %s" %(case_num,solve(line))


if __name__ == '__main__':
	main()