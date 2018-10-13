
def solve(s,k):
    idx = next((i for i,v in enumerate(s) if v==0),-1)
    if idx==-1:
        return 0
    flips = 0
    while idx != -1:
        if idx > len(s)-k:
            return 'IMPOSSIBLE'
        for i in range(k):
            s[idx+i] = not(s[idx+i])
        idx = next((i for i,v in enumerate(s) if v==0),-1)
        flips += 1
    return flips

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t+1):
        s,k = [ele for ele in raw_input().split(' ')]
        k = int(k)
        s = s.replace('+','1').replace('-','0')
        s = [int(ele) for ele in s]
        soln = solve(s,k)
        print('Case #{}: {}'.format(i, soln))