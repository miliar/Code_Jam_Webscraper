import sys
import math

def factor(n):
	f = []
	sqrt = math.sqrt(n)
	i = 2
	while i <= sqrt:
		if n % i == 0:
			f.append(i)
			n /= i
			i = 2
		else:
			i += 1
	if n > 1:
		f.append(int(n))
	return f

output = []

f = open(sys.argv[1])
try:
    for N in range(int(f.next())):
        A, B, P = tuple(map(int, f.next().split()))
        
        sets = [frozenset([n]) for n in range(A, B + 1)]
        
        def merge(i, j):
            i = [s for s in sets if i in s][0]
            j = [s for s in sets if j in s][0]
            sets.remove(i)
            if j in sets:
                sets.remove(j)
            sets.append(i | j)
        
        for i in range(A, B + 1):
            for j in range(A, B + 1):
                if not j > i:
                    continue
                a = set(n for n in factor(i) if n >= P)
                b = set(n for n in factor(j) if n >= P)
                if len(a & b) > 0:
                    merge(i, j)
        
        output.append(len(sets))
finally:
    f.close()

f = open(sys.argv[2], 'w')
try:
    f.write('\n'.join('Case #%s: %s' % (i + 1, n) for i, n in enumerate(output)))
finally:
    f.close()