
# mapping = dict(
# 	zip("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand") + 
# 	zip("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities") + 
# 	zip("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")
# )
# mapping['z'] = 'q'
# mapping['q'] = 'z'

# with open('A-small-attempt1.in') as input:
# 	N = int(input.readline())
# 	with open('A-small-attempt1.out', 'w') as output:
# 		for i, line in enumerate(input.readlines()):
# 			output.write("Case #{i}: {decoded}\n".format(i=i+1, decoded=''.join([mapping[ch] for ch in line[:-1]])))

def tokenizer(stream):
	for line in stream:
		for token in line.split(' '):
			yield int(token)

from collections import deque

with open('C-small-attempt0.in') as input:
	tokenized = tokenizer(input.readlines())
	N = tokenized.next()
	with open('C-small-attempt0.out', 'w') as output:
		for i in xrange(N):
			treated = set()
			pairs = {}
			n, m = tokenized.next(), tokenized.next()
			for j in xrange(n, m+1):
				if j in treated:
					continue
				treated.add(j)
				l = len(str(j))
				numbers = deque(str(j))
				for r in xrange(len(str(j))):
					numbers.rotate()
					new = int(''.join(numbers))
					if new != j and len(str(new)) == l and n <= new <= m:
						treated.add(new)
						pairs.setdefault(j,set()).add(new)
			#print pairs
			solution = reduce(lambda i, p: i+len(p)*(len(p)+1)/2, pairs.values(), 0)
			output.write("Case #{i}: {solution}\n".format(i=i+1, solution=solution))