
import sys

def solve(exists, creates):
    result = 0
    root = {}
    for e in exists:
        parent = root
        for d in e.split('/')[1:]:
            if not d in parent:
                parent[d] = {}
            parent = parent[d]
            
    for c in creates:
        parent = root
        for d in c.split('/')[1:]:
            if not d in parent:
                result += 1
                parent[d] = {}
            parent = parent[d]
    
    return result
        
        
def main():
    input = open(sys.argv[1])
    t = int(input.next())
    
    for i in range(t):
        n, m = [int(a) for a in input.next().split()]
        exists = [input.next().strip() for a in range(n)]
        creates = [input.next().strip() for a in range(m)]
        
        print "Case #%d: %d" % (i+1, solve(exists, creates))

if __name__ == "__main__":
    main()
    