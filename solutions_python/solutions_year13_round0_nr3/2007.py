# helpers (http://code.activestate.com/recipes/577565-binary-search-function/)

import __builtin__

def lower_bound(haystack, needle, lo = 0, hi = None, cmp = None, key = None):
    if cmp is None: cmp = __builtin__.cmp
    if key is None: key = lambda x: x
    if lo < 0: raise ValueError( 'lo cannot be negative' )
    if hi is None: hi = len(haystack)

    val = None
    while lo < hi:
        mid = (lo + hi) >> 1
        val = cmp(key(haystack[mid]), needle)
        if val < 0:
            lo = mid + 1
        else:
            hi = mid
    return lo

def upper_bound(haystack, needle, lo = 0, hi = None, cmp = None, key = None):
    if cmp is None: cmp = __builtin__.cmp
    if key is None: key = lambda x: x
    if lo < 0: raise ValueError( 'lo cannot be negative' )
    if hi is None: hi = len(haystack)

    val = None
    while lo < hi:
        mid = (lo + hi) >> 1
        val = cmp(key(haystack[mid]), needle)
        if val > 0:
            hi = mid
        else:
            lo = mid + 1
    return lo

# end of helpers

fair_square = [1, 4, 9]
seq_max = 3

def setup():
	def insert(seq):
		num = long(seq)
		fair_square.append(num * num)
		
	for i in xrange(seq_max / 2):
		seq = '2' + ('0' * i)
		revseq = ''.join(reversed(seq))
		
		insert(seq + revseq)
		insert(seq + '1' + revseq)
	
	q = [('1', 8)]
	
	while len(q) > 0:
		cur = q.pop()
		
		seq = cur[0]
		revseq = ''.join(reversed(seq))
		seqlen = len(seq)
		
		insert(seq + revseq)
		
		if cur[1] > 1 and seqlen < seq_max / 2:
			insert(seq + '1' + revseq)
		
		if cur[1] > 7 and seqlen < seq_max / 2:
			insert(seq + '2' + revseq)
		
		if seqlen == seq_max / 2:
			continue
		
		q.append((seq + '0', cur[1]))
		
		if cur[1] > 1:
			q.append((seq + '1', cur[1] - 1))
	
	fair_square.sort()

def case(n):
	A, B = map(int, raw_input().split(' '))
	
	r = lower_bound(fair_square, B)
	l = lower_bound(fair_square, A)
	
	ans = abs(r - l)
	
	if r < len(fair_square) and fair_square[r] == B:
		ans += 1
	
	print 'Case #%d: %d' % (n, ans)

if __name__ == '__main__':
	setup()
	
	for i in xrange(int(raw_input())):
		case(i + 1)