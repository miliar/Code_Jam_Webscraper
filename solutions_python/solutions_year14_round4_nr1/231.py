from bisect import bisect


        
def small(t, Ns, X):
    Ns.sort()
    count = 0
    while Ns:
        last = Ns.pop()
        cap = X - last
        if len(Ns) > 0 and cap >= Ns[0]:
            i = bisect(Ns, cap)
            first = Ns.pop(i-1)
            assert first + last <= X
        count += 1
    print 'Case #{0}: {1}'.format(t, count)
       
        
 
def main():
    T = int(raw_input())
    for t in xrange(1, T + 1):
        _, X = map(int, raw_input().split())
        Ns = map(int, raw_input().split())
        small(t, Ns, X)
 
 
if __name__ == '__main__':
    main()
