import math
x = open("A-large.in")
z = open("A-large.out", "w")
n = int(x.readline()[:-1])
zs = ""

for i in range(n):
    a, b = x.readline()[:-1].split()
    a = int(a)
    b = int(b)
    r = []
    h = []
    rh = []
    r2 =  []
    h2 = []
    rh2 = []
    for j in range(a):
        cr, ch = x.readline()[:-1].split()
        r.append(int(cr))
        h.append(int(ch))
        rh.append(int(cr)*int(ch)*2)
    for j in range(b):
        m = max(rh)
        mi = rh.index(m)
        r2.append(r[mi])
        h2.append(h[mi])
        rh2.append(rh[mi])
        del r[mi]
        del h[mi]
        del rh[mi]
    if max(r + r2) in r2:
        summe = (sum(rh2) + max(r + r2)**2) * math.pi
        zs += "Case #" + str(i + 1) + ": " + str(summe) + "\n"
    else:
        y = max(r2)
        rhmin = min(rh2)
        rhminc = min(rh2)
        while max(r) > max(r2):
            rmax = max(r)
            rmaxin = r.index(rmax)
            rplus = (rmax**2 - max(r2)**2) + rmax*h[rmaxin]*2
            if rplus > rhminc:
                rhminc = rplus
                rmaxm = rmax
                hmaxm = h[rmaxin]
                rhmaxm = rh[rmaxin]
            del r[rmaxin]
            del h[rmaxin]
            del rh[rmaxin]
            if len(r) == 0 or len(r2) == 0:
                break
        if rhminc == rhmin:
            summe = (sum(rh2) + max(r + r2)**2) * math.pi
            zs += "Case #" + str(i + 1) + ": " + str(summe) + "\n"
        else:
            rhminin = rh2.index(rhmin)
            del r2[rhminin]
            del h2[rhminin]
            del rh2[rhminin]
            r2.append(rmaxm)
            h2.append(hmaxm)
            rh2.append(rhmaxm)
            summe = (sum(rh2) + max(r + r2)**2) * math.pi
            zs += "Case #" + str(i + 1) + ": " + str(summe) + "\n"
z.write(zs[:-1])
z.close()
