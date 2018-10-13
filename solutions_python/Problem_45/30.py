import sys

def solve(prisoners, releases):
    
    if len(releases) == 0:
        return 0
    
    m = None
    for r in releases:
        r=r-1
        total = 0
        tprisoners = prisoners[:]
        tprisoners[r] = -1
        for i in range(r-1, -1, -1):
            if tprisoners[i] == -1:
                break
            else:
                total += 1
        for i in range(r+1, len(tprisoners), 1):
            if tprisoners[i] == -1:
                break
            else:
                total += 1
        treleases = releases[:]
        treleases.remove(r+1)
        
        a = total + solve(tprisoners, treleases)
        if m is None:
            m = a
        else:
            m = min(m, a)
    
    return m


def main():
    input = open(sys.argv[1])
    num_cases = int(input.readline())
    
    for i in range(num_cases):
        p,q = [int(t) for t in input.readline().split()]
        prisoners = [n for n in range(p)]
        releases = [int(t) for t in input.readline().split()]
        
        print 'Case #%d:' % (i+1), solve(prisoners, releases)
        

if __name__ == '__main__':
    main()
    
        
        
        