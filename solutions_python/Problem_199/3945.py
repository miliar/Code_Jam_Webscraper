def fn(inp, k):
    
    from collections import deque
    
    times = 0
    visited = set([inp])
    curr_level = deque([inp])
    next_level = deque([])

    while(True):
        
        while(len(curr_level) > 0):
        
            u = curr_level.popleft()

            if u == '+'*len(inp):
                return times
        
            for i in range(len(inp) - k + 1):
                flipped = list(u)
                for j in range(i, i+k):
                    if flipped[j] == '+':
                        flipped[j] = '-'
                    else:
                        flipped[j] = '+'
                flipped = ''.join(flipped)
                if flipped not in visited: 
                    next_level.append(flipped)
                    visited.add(flipped)
        
        if len(next_level) != 0:
            times += 1
            curr_level = next_level
            next_level = deque([])
        else:
            break
    
    return None

N = int(raw_input())
test_cases = []
Ks = []

for _ in range(N):
    line = raw_input()
    test_cases.append(line.split(' ')[0])
    Ks.append(int(line.split(' ')[1]))

for i in range(len(test_cases)):
    res = fn(test_cases[i], Ks[i])
    if res != None:
        print "Case #{0}: {1}".format(i+1, res)
    else:
        print "Case #{0}: {1}".format(i+1, "IMPOSSIBLE")
            
        