def solve(hd,ad,hk,ak,b,d,cure,seen,mem):
   # print (hd,ad,hk,ak,b,d,cure)
    if hd <=0:
        return -1
    if hk <=0:
        return 0
    if (hd,ad,hk,ak,b,d,cure) in mem:
        return mem[(hd,ad,hk,ak,b,d,cure)]
    if (hd,ad,hk,ak,b,d,cure) in seen:
        return -1
    seen[(hd,ad,hk,ak,b,d,cure)] = True
    if hk <= ad:#attack, kill
        mem[(hd, ad, hk, ak, b, d, cure)] = 1
        return 1
    ra = -1
    rb = -1
    rc = -1
    rd = -1
    ra = solve(hd-ak,ad,hk-ad,ak,b,d,cure,seen,mem)#attack
    if b!=0:
        rb = solve(hd-ak,ad+b,hk,ak,b,d,cure,seen,mem)#buff
    new_ak = ak - d
    if new_ak < 0:
        new_ak = 0
    if d != 0:
        rd  =solve(hd - new_ak, ad, hk, new_ak, b, d, cure, seen, mem) #deb
    rc = solve(cure-ak,ad,hk,ak,b,d,cure,seen,mem)
    rc = solve(cure - ak, ad, hk , ak, b, d, cure, seen, mem)
    xx = [ra,rb,rc,rd]
    xxx = [x for x in xx if x != -1]
    r  = -1
    if len(xxx) != 0:
        r = min(xxx)
        r+=1
    mem[(hd,ad,hk,ak,b,d,cure)] = r
    return r





f = open("C:\\Users\\TocarIP\\Google Drive\\Downloads\\C-small-attempt2.in")
lines = f.readlines()
numcases = int(lines[0])
i = 1
while i <= numcases:
    hd,ad,hk,ak,b,d = [int(x) for x in lines[i].split()]
    cure = hd
    seen = {}
    mem = {}
    ret = solve(hd,ad,hk,ak,b,d,cure,seen,mem)
    #print (mem)
    res = "Case #" + str(i) + ": "
    if ret == -1:
        print (res + "IMPOSSIBLE")
    else:
        print(res + str(ret))
    i = i+ 1