def solve():
    t = int(raw_input())
    for x in range(t):
        stager1 = []
        stager2 = []
        r1 = int(raw_input())
        for y in range(4): stager1.append([int(z) for z in raw_input().split()])
        r2 = int(raw_input())
        for y in range(4): stager2.append([int(z) for z in raw_input().split()])
        ans = [a for a in stager1[r1-1] if a in stager2[r2-1]]
##        print ans
##        print stager1
##        print stager2
        if len(ans) == 0: print 'Case #%d: Volunteer cheated!' % (x + 1)
        elif len(ans) > 1: print 'Case #%d: Bad magician!' % (x + 1)
        else: print 'Case #%d: %d' % (x + 1, ans[0])
    return

if __name__ == '__main__': solve()
            
    
