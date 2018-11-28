# 5
# 4 2
# 5 2
# 6 2
# 1000 1000
# 1000 1
import sys, re, math

r_stalls = re.compile(r'(\d+) (\d+)')
def solve(line):
	m = r_stalls.match(line)
	if not m: return "Invalid  Input"

	gaps = [int(m.group(1))]
	L, R = 0, 0
	for _ in xrange(int(m.group(2))):
		pos, gap = largest(gaps)
		gap -= 1
		L, R = int(math.floor(gap/2.0)), int(math.ceil(gap/2.0))
		gaps[pos] = L
		gaps.insert(pos+1, R)

	return ' '.join([str(max(L, R)), str(min(L, R))])

def largest(l):
	pos = max(xrange(len(l)), key=l.__getitem__)
	return pos, l[pos]

def handle_io():
	for idx, line in enumerate(sys.stdin):
	  if not idx: continue
	  print "Case #{}: {}".format(idx, solve(line.strip()))

if __name__ == '__main__':
	handle_io()
