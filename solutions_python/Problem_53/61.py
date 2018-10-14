import sys

def on_or_off(N, K):
    
    """
    # enumeration
    snappers = [False] * N
    light = False
    
    for R in range(K):
        new_snappers = snappers[:]
        print 'R', R, snappers, light
        for i in range(len(snappers)):
            if i-1 < 0 or snappers[i-1]:
                new_snappers[i] = not snappers[i]
            else:
                break
            
        snappers = new_snappers
        light = all(snappers)
                
    print 'final snappers', snappers, light
    return light
    """
    
    return False if (K + 1) % (2**N) else True 


if __name__ == '__main__':
    ntests = int(sys.stdin.readline())
    for i in range(1, ntests+1):
        N, K = sys.stdin.readline().split()
        is_on = on_or_off(int(N), int(K))
        ans = 'ON' if is_on else 'OFF'
        print 'Case #%s: %s' %  (i, ans)
