import operator

def solve(C, F, X):
	
	delta = 2.0
	te = 0
	tp = 0
	
	while(True):
		tpn = X / delta + te
		
		if tp > 0 and tpn > tp:
			return tp

		te += C / delta
		delta += F
		tp = tpn


def string_to_vect(value):
	return map(float, value.split(" "))

if __name__ == "__main__":
	test_cases = input()
     
	for case in xrange(1, test_cases + 1):
		C, F, X = string_to_vect(raw_input())
		
		print "Case #%i: %s" % (case, solve(C, F, X))
