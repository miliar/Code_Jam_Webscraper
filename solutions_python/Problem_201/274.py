T = input()
    
for t in range(1, T+1):
    print 'Case #%d:' % t,
    N, K = map(int, raw_input().split())
    done = set()
    def f(n):
        if n == 0 or n in done: return
        done.add(n)
        f((n-1) // 2);  f(n // 2)
    f(N)
    cnt = {x : int(x == N) for x in done | {0, -1}}
    for x in sorted(done, reverse = True):
        cnt[x     // 2] += cnt[x]
        cnt[(x-1) // 2] += cnt[x]
    cnt = sorted(cnt.items(), reverse =  True)
    s = 0
    for i in range(len(cnt)):
        s += cnt[i][1]
        if s >= K:
            break
    print cnt[i][0] // 2, (cnt[i][0]-1) // 2
            
        


    
    
