
def main():
    count = input()

    for i in xrange(count):
	    print 'Case #%s: %s' % (i + 1, solve(raw_input()))

def solve(inputs):
	inputs = map(int, inputs.split())
	n = inputs[0]
	s = inputs[1]
	p = inputs[2]
	points = inputs[3:]

	return min([
		len([x for x in points if high(x) >= p]) + s,
		len([x for x in points if sup_high(x) >= p])
	])

def high(p):
	return p / 3 + (p % 3 > 0)

def sup_high(p):
	if p <= 1:
		return p
	
	return p / 3 + 1 + (p % 3 == 2)

main()