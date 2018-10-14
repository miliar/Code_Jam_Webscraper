from sys import stdin as fp

def flip(lst, pos, K):
    for i in range(K):
        if lst[pos + i] == '-':
            lst[pos + i] = '+'
        else:
            lst[pos + i] = '-'

def pancake_turns(ps, K):
    cnt = 0
    for i, p in enumerate(ps):
        #print(ps, i)
        if p == '-':
            cnt += 1
            if i + K > len(ps):
                return 'IMPOSSIBLE'
            flip(ps, i, K)
    return cnt
            

    
T = int(fp.readline())
for i, line in enumerate(fp):
    p, K  = line.split()
    p = list(p)
    K = int(K)
    print("Case #{}: {}".format(i+1, pancake_turns(p, K)))

