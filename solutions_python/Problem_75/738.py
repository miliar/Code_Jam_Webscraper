import sys
from collections import defaultdict

if __name__ == '__main__':
    sys.stdin.readline()
    for case, line in enumerate(sys.stdin):
        comb = {}
        oppos = defaultdict(list)
        
        parts = line.strip().split()        
        C = int(parts[0])
        for i in xrange(1, C + 1):
            comb[tuple(sorted(parts[i][:2]))] = parts[i][2]
        
        D = int(parts[C + 1])
        for i in xrange(C + 2, C + 2 + D):
            oppos[parts[i][0]].append(parts[i][1])
            oppos[parts[i][1]].append(parts[i][0])
        
        input = list(parts[-1])
        
        res = []
        for c in input:
            res.append(c)
            suffix = tuple(sorted(res[-2:]))
            
            if suffix in comb:
                res[-2:] = comb[suffix]
            elif any(x in res for x in oppos.get(c, [])):
                res = []
        
        sys.stdout.write('Case #%s: [%s]\n' % (case + 1, ', '.join(res)))