def evmax(pi, ni, ki):
    return max([(p+k-1)//k for p, k in zip(pi, ki)]) + sum([n*(k-1) for n, k in zip(ni, ki)])

def findmin(pi, ni, cki, i):
    if i == len(ni)-1:
        return min([evmax(pi, ni, cki+[j]) for j in range(1, pi[i]+1)])
    return min([findmin(pi, ni, cki+[j], i+1) for j in range(1, pi[i]+1)])

t = int(input())
for tc in range(1, t+1):
    d = int(input())
    pl = [int(x) for x in input().split()]
    pi = list(set(pl))
    pi.sort()
    ni = [pl.count(x) for x in pi]
    tmin = findmin(pi, ni, [], 0)
    print('Case #%i: %i' % (tc, tmin))

    
    
        
