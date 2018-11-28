import sys
import math

def solve(creators, opposed, seq):
    res = []
    counts = [0] * 26
    for c in seq:
        if len(res)>=1 and res[-1]+c in creators:
            counts[ord(res[-1]) - ord('A')] -= 1
            res[-1] = creators[res[-1]+c]
            counts[ord(res[-1]) - ord('A')] += 1
        else:
            deleted = False
            for op in opposed:
                if op[0] == c and counts[ord(op[1]) - ord('A')]>0:
                    res = []
                    counts = [0] * 26
                    deleted = True
                    break
            if not deleted:
                res.append(c)
                counts[ord(c) - ord('A')] += 1
    return res                    
                    

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    C = int(line[0])
    creatorsS = line[1:1+C]
    line = line[1+C:]
    D = int(line[0])
    opposedS = line[1:1+D]
    line = line[1+D:]
    N = line[0]
    seq = line[1]
    creators = {}
    for c in creatorsS:
        creators[c[:2]] = c[2]
        creators[c[1]+c[0]] = c[2]
    opposed = []
    for op in opposedS:
        opposed.append(op)
        opposed.append(op[1]+op[0])
    res = solve(creators, opposed, seq)
    return '[' + ', '.join(res) + ']'

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
