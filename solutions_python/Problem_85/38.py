import copy

infile = open('B-large.in').readlines()
infile = [line.strip() for line in infile]
wfile = open('result', 'w')
T = int(infile[0])
infile = infile[1:]

def test(L, t, N, C, Clist):
    dup = N / C
    remain = N % C
    dist = sum(Clist) * dup + sum(Clist[:remain])
    if t >= dist * 2:
        return dist * 2
    if L == 0:
        return dist * 2
    
    # cal the next star when boosters are finished
    tsum = t
    nC = t / (sum(Clist) * 2)
    tres = t % (sum(Clist) * 2)
    star = 0
    while True:
        if tres >= Clist[star] * 2:
            tres -= Clist[star] * 2
            star += 1
        else:
            break
    
    rest = Clist[star] - tres / 2.0
    
    # if it's the last round
    if nC == dup-1:
        reststar = [rest,]
        reststar.extend(Clist[star+1:])
        if len(reststar) < L:
            tsum += sum(reststar)
            return tsum
        else:
            reststar.sort(reverse=True)
            tsum += sum(reststar[:L])
            tsum += sum(reststar[L:]) * 2
            return tsum
            
    dup = dup - nC - 1
    reststar = [rest,]
    reststar.extend(Clist[star+1:])
    reststar.extend(Clist[:remain])
    reststar.sort(reverse=True)
    tmp = copy.copy(Clist)
    tmp.sort(reverse=True)
    if L >= dup * len(tmp) + len(reststar):
        tsum += dup * sum(tmp)
        tsum += sum(reststar)
        return tsum
        
    while L > 0:
        #if len(tmp) == 0:
        #    break
        if len(reststar) ==0 or tmp[0] > reststar[0]:
            if L >= dup:
                tsum += tmp[0] * dup
                L -= dup
                tmp = tmp[1:]
            else:
                tsum = tsum + tmp[0] * L + (dup-L) * tmp[0] * 2
                L = 0
                tmp = tmp[1:]
        else:
            tsum += reststar[0]
            reststar = reststar[1:]
            L -= 1
            
    tsum += (dup * sum(tmp) * 2 + sum(reststar) * 2)
    return tsum
    
    

for case_no in range(1, T+1):
    line = infile[0]
    infile = infile[1:]
    tmp = [int(x) for x in line.split()]
    L = tmp[0]
    t = tmp[1]
    N = tmp[2]
    C = tmp[3]
    Clist = tmp[4:]
    res = test(L, t, N, C, Clist)
    wfile.write('Case #' + str(case_no) + ': ' + str(int(res)) + '\n')