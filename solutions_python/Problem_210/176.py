HALF = 720

def findsh(act, who):
    n = len(act)
    sh = 2000
    shind = -1
    for i in range(n):
        #print("findsh", i, who)
        if act[i][2] != who or act[i][2] != act[(i+1)%n][2]:
            #print("findsh skip")
            continue
        else:
            if i == n-1:
                diff = act[(i+1)%n][0] + 2*HALF - act[i][1]
            else:
                diff = act[(i+1)%n][0] - act[i][1]
            if diff < sh:
                sh = diff
                shind = i
    return shind, sh

def solve():
    ac, aj = map(int, input().split())
    act = []
    ctime = 0 #how long c can't have it
    for i in range(ac):
        c,d = map(int, input().split())
        act.append((c,d,0,))
        ctime += d - c
    jtime = 0
    for i in range(aj):
        c, d = map(int, input().split())
        act.append((c,d,1,))
        jtime += d-c
    act.sort()
    
    who = 0
    while True:
        ind, sh = findsh(act,who)
        if who == 0 and (ind == -1 or ctime + sh > HALF):
            #print("end c")
            who = 1
            continue
        elif ind == -1 or jtime + sh > HALF:
            #print("end j")
            break
        n = len(act)
        if ind == n - 1:
            diff = act[(ind+1)%n][0] + 2*HALF - act[ind][1]
            act[ind] = (act[ind][0], act[(ind+1)%n][1] + 2*HALF, act[ind][2])
        else:
            diff = act[(ind+1)%n][0] - act[ind][1]
            act[ind] = (act[ind][0], act[(ind+1)%n][1], act[ind][2])
        #print(diff, sh, ind, act)
        assert(diff >= 0)
        assert(diff == sh)
        if who == 0:
            ctime += diff
        else:
            jtime += diff
        act.pop((ind+1)%n)
    
    #print(act, jtime, ctime)
    
    swaps = 0
    n = len(act)
    for i in range(n):
        if act[i][2] != act[(i+1)%n][2]:
            swaps += 1
        else:
            swaps += 2
    
    print(swaps)


if __name__ == '__main__':
    t = int(input())
    for tc in range(1,t+1):
        print("Case #{}: ".format(tc), end='')
        solve()
        #print('')
