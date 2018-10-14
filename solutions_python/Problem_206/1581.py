
fout = open('2b-f6-large.out', 'w')

def lp(s, n):
    return (n-len(s))*'0'+s

def doprint(s):
    print(s)
    fout.write(s+'\n')

def close():
    fout.close()

inf = 10**100

T = int(input())
for tc in range(1, T+1):
    D, N = list(map(int, input().split()))#int(input())
    v = []
    for i in range(N):
        va = list(map(int, input().split()))
        v.append(va)

    atime = 0
    '''for i in range(N):
        mi = -1
        mt = inf

        pi = 0
        while v[pi][0] == None: pi += 1

        j = pi + 1
        while j < N:#for j in range(1, N):
            if v[j][0] == None:
                j += 1
                continue
            else:
                cdist = v[j][0] - v[pi][0]
                ctime = cdist / float(v[pi][1] - v[pi][0])
                if ctime > 0:
                    if ctime < mt:
                        mi = pi # the one to be removed
                        mt = ctime
         atime += ctime
    '''
    Mi = -1
    Mt = 0
    for i in range(N):
        ct = (D-v[i][0]) / v[i][1]
        if ct > Mt:
            Mt = ct
            Mi = i
    
        
    
    rate = D / Mt
    ans = rate
    doprint("Case #"+str(tc)+": "+str(ans))

close()

'''
3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam
'''
