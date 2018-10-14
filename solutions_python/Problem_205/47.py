fin = open("C-small-attempt2.in","rt")
import math
t = fin.readline().rstrip('\n')
t = int(t)

fout = open("OUTPUT","wt")

def simbat(hd,ad,hk,ak,hmax):
    turn = 0
    while hk > 0:
        turn += 1
        if ad >= hk: return turn
        if hd <= ak:
            hd = hmax
            hd -= ak
            if hd<=ak: return -1
            continue
        hk -= ad
        hd -= ak
        if hd<=0: return -1

def simb(hd,ad,hk,ak,hmax,b,buf):
    turn = 0
    while buf > 0:
        turn += 1
        if hd <= ak:
            hd = hmax
            hd -= ak
            if hd<=ak: return -1
            continue
        ad += b
        buf -= 1
        hd -= ak
    check = simbat(hd,ad,hk,ak,hmax)
    if check == -1: return -1
    else: return check+turn

def simall(hd,ad,hk,ak,b,d,deb):
    hmax = hd
    turn = 0
    while deb > 0:
        turn += 1
        if hd <= ak-d:
            hd = hmax
            hd -= ak
            if hd<=ak: return -1
            continue
        ak -= d
        deb -= 1
        hd -= ak
    opt = 1000
    for buf in range(0,200-deb):
        check = simb(hd,ad,hk,ak,hmax,b,buf)
        if check == -1: continue
        opt = min(opt,check)
    if opt == 1000: return -1
    return turn + opt

def opter(hd,ad,hk,ak,b,d):
    opt = 1000
    for deb in range(0,200):
        check = simall(hd,ad,hk,ak,b,d,deb)
        if check == -1: continue
        opt = min(opt,check)
    if opt == 1000: return "IMPOSSIBLE"
    else: return str(opt)

for ex in range(t):
    result = ""
    stat = fin.readline().rstrip('\n').split(' ')
    stat = [int(x) for x in stat]
    hd = stat[0]
    ad = stat[1]
    hk = stat[2]
    ak = stat[3]
    b = stat[4]
    d = stat[5]

    result = opter(hd,ad,hk,ak,b,d)

    
    
    s = "Case #"+str(ex+1)+": "+result+"\n"
    fout.write(s)
    print s


fout.close()
