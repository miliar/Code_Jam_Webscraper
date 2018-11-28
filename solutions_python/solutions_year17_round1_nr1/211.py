from collections import defaultdict
def solve():
    R, C = raw_input().split()
    pos = defaultdict(list)
    R = int(R)
    C = int(C)
    lines = []
    for i in range(R):
        l = list(raw_input().strip())
        lines.append(l)
    for r in range(len(lines)):
        seen = False
        for c in range(C):
            if lines[r][c] != '?':
                seen = lines[r][c]
                k = c-1
                while k >= 0 and lines[r][k] == '?':
                    lines[r][k] = lines[r][c]
                    k -= 1
            if c == C-1 and lines[r][c] == '?' and seen != False:
                k = c
                while k >= 0 and lines[r][k] == '?':
                    lines[r][k] = seen
                    k -= 1
        counter = 0
    for r in range(R):
        counter += 1
        if set(lines[r]) != set('?'):
            last = lines[r]
            for _ in range(counter):
                print ''.join(last)
            counter = 0
            
    for _ in range(counter):
        print ''.join(last)





if __name__ == '__main__':
    T = int(raw_input())
    for i in range(1, T+1):
        print "Case #{}:".format(i)
        solve()
