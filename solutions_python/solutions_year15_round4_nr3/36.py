def helper(english, france, lines, c):
        if lines == []:
                return len(english.intersection(france))
        if len(english.intersection(france)) > c:
                return c
        if lines[0].issubset(english):
                return helper(english, france, lines[1:], c)
        elif lines[0].issubset(france):
                return helper(english, france, lines[1:], c)
        a = helper(english.union(lines[0]), france, lines[1:], c)
        b = helper(english, france.union(lines[0]), lines[1:], a)
        return min(a, b)

	
def solve(_lines):
       english = set(_lines[0].split())
       france = set(_lines[1].split())
       lines = []
       for i in _lines[2:]:
               a = set(i.split())
               if not a.issubset(english) and not a.issubset(france):
                       lines.append(a)
       return helper(english, france, lines, 200000)
	
		
import threading
output = []
class X(threading.Thread):
        def __init__(self, i, lines):
                threading.Thread.__init__(self)
                self.i = i+1
                self.lines = lines
        def run(self):
                global output
                l = (self.i, solve(self.lines))
                output.append(l)


T = int(raw_input())
threads = []
for i in xrange(T):
        N = int(raw_input())
        lines = []
        for j in xrange(N):
                lines.append(raw_input())
        threads.append(X(i, lines))

for t in threads:
        t.start()
        
for t in threads:
        t.join()

o = sorted(output)

for l in o:
        print 'Case #%d: %d' % l
