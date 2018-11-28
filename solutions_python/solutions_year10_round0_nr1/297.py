import sys

class Circuit(object):
    def __init__(self, n):
        self.num_snappers = n
        self.snappers_powered = 1
        self.snapper_states = [False] * n
        
    def toggle(self):
        first_off = None
        # toggle state of every powered snapper, and record first off state
        for i in xrange(self.snappers_powered):
            self.snapper_states[i] = not self.snapper_states[i]
            if (first_off is None) and (not self.snapper_states[i]):
                first_off = i
        
        if first_off is None:
            # continue looking at previously unpowered snappers, as long as they're on the power will keep flowing
            for i in xrange(self.snappers_powered, self.num_snappers):
                if not self.snapper_states[i]:
                    first_off = i
                    break
        
        if first_off is not None:
            self.snappers_powered = first_off + 1
        else:
            self.snappers_powered = self.num_snappers
            

infile = sys.stdin
ntests = int(infile.readline().strip())        
for i in xrange(ntests):
    N, K = map(int, infile.readline().strip().split())
    c = Circuit(N)
    for j in xrange(K):
        c.toggle()
        
    result = (c.snapper_states[-1] and c.snappers_powered==N)
    print("Case #%d: %s" % (i+1, "ON" if result else "OFF"))
    