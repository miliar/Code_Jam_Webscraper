PI = 3.14159265358979


def rest(pc, k):
    assert(k <= len(pc))
    newl = []
    for p in pc:
        newl.append(2*p[0]*p[1])
    newl.sort()
    newl.reverse()
    v = 0
    for i in range(k):
        v += newl[i]
    return v
    
def solve():
    n, k = map(int, input().split())
    #first pancake (largest r) gives r^2 + 2rh, others give 2rh
    #can only use those with r <= that of first for calc to be correct
    pc = []
    for i in range(n):
        r,h = map(int, input().split())
        pc.append((r,h,))
    pc.sort()
    pc.reverse()
    maxv = -1
    for i in range(n-k+1):
        firsta = pc[i][0]**2 + 2*pc[i][0]*pc[i][1]
        resta = rest(pc[i+1:], k-1)
        maxv = max(maxv, firsta + resta)
    print(PI*maxv)

if __name__ == '__main__':
    t = int(input())
    for tc in range(1,t+1):
        print("Case #{}: ".format(tc), end='')
        solve()
        #print('')
