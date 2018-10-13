import re

def solve():
    global case, f
    
    [R, k, N] = re.findall(r'\d+', f.readline())
    g = re.findall(r'\d+', f.readline())
    
    R = int(R)
    k = int(k)
    N = int(N)
    
    for i in range(0,len(g)):
        g[i] = int(g[i])
    
    T = 0

    next = 0
    for i in range(0, R):
        current = 0
        
        for j in range(0, N):
            current = current + g[next]
            
            if current <= k:
                T = T + g[next]
            else:
                break
            
            next = next + 1
            if (next >= len(g)):
                next = 0
    
    print("Case #" + str(case) + ": "  + str(T))


# BEGIN APP

file = 'C-small-attempt0.in'

f = open(file, 'r');
cases = int(f.readline());

for case in range(1,cases+1):
    solve()


f.close()
