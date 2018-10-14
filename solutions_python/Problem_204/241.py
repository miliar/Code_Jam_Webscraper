class Package(object):
    __slots__ = ['quantity', 'required', 'servings']
    def __init__(self, quantity, required):
        self.quantity = quantity
        self.required = required
        minServings = 0
        maxServings = 0
        n1 = int(quantity / (1.1*required))
        n2 = int(quantity / (0.9*required))
        for n in xrange(n1, n2+1):
            if 0.9*n*required <= self.quantity and self.quantity <= 1.1*n*required:
                if minServings == 0:
                    minServings = n
                if n > maxServings:
                    maxServings = n
        self.servings = (minServings, maxServings)

    def __cmp__(self, other):
        return cmp(other.quantity, self.quantity)

def overlaps(a, b):
    if a[1] < b[0]: return False
    if b[1] < a[0]: return False
    return True
    
def maxKits(packages):
    n = len(packages)
    kits = 0
    while packages[0]:
        p0 = packages[0].pop()
        s = p0.servings
        if s[1] == 0: continue
        # Run through each ingredient's package list.
        # Discard any packages whose max servings are less than the min of s
        for i in xrange(1, n):
            while packages[i] and packages[i][-1].servings[1] < s[0]:
                packages[i].pop()
        canFormKit = True
        # Run through the list again looking for overlaps
        for i in xrange(1, n):
            if not packages[i] or not overlaps(s, packages[i][-1].servings):
                canFormKit = False
                break
        if canFormKit:
            for i in xrange(1, n): packages[i].pop()
            kits += 1
    return kits
        

if __name__ == "__main__":
    T = int(raw_input())
    for t in xrange(1, T+1):
        N, P = map(int, raw_input().split())
        R = map(int, raw_input().split())
        packages = []
        for i in xrange(N):
            packages.append([Package(x, R[i]) for x in map(int, raw_input().split())])
            packages[i].sort()            

        print "Case #%d: %d" % (t, maxKits(packages))
        
