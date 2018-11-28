from itertools import count

# turns out we don't need all this
if 0:
    class Chain(object):
        def __init__(self, n):
            self.data = [False]*n
            
        def snap(self):
            for i, snapper in enumerate(self.data):
                if not snapper: break
            for j in range(i+1):
                self.data[j] = not self.data[j]

        def __str__(self):
            s = '['
            for snapper in self.data:
                s += '1' if snapper else '0'
            s += ']'
            return s

# From http://code.activestate.com/recipes/52201/ - I hope that's allowed!
class Memoize:
    """Memoize(fn) - an instance which acts like fn but memoizes its arguments
       Will only work on functions with non-mutable arguments"""
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if not self.memo.has_key(args):
            self.memo[args] = self.fn(*args)
        return self.memo[args]

def snapperProblem(n, k):
    return (k+1) % (2**n) == 0

snapperProblem = Memoize(snapperProblem)

def reprAnswer(b):
    if b:
        return "ON"
    else:
        return "OFF"

input_file = file('A-large.in', 'r')
t = input_file.next()
results = []
try:
    for i in count(1):
        n, k = (int(x) for x in input_file.next().split())
        results.append(snapperProblem(n, k))
except StopIteration:
    input_file.close()

for i,r in enumerate(results):
    print "Case #%s: %s" % ((i+1), reprAnswer(r))
