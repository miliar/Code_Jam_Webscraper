import sys

def func(s):
    asc = True
    a = [c for c in s]
    for i in range(len(s) - 1):
        if s[i] < s[i+1]:
            asc = False
            break
    if asc:
        a.sort()
        if a[0] == '0':
            i = 1
            while a[i] == '0':    
                i += 1
            a[0] = a[i]
            a[i] = '0'
        a.insert(1, '0')
        return "".join(a)
    i = len(s) - 1
    all = []
    while i > 0:
        c = s[i]
        for j in range(i):
            k = i - j - 1
            #print "-", i, c, j, k, s[k]
            if s[k] < c:
                tmpa = [xx for xx in a]
                tmpa[i] = a[k]
                tmpa[k] = c
                aa = tmpa[k+1:]
                aa.sort()
                for m in range(len(aa)):
                    tmpa[k + m + 1] = aa[m]
                tmp = "".join(tmpa)
                #print ">", tmp
                all.append(tmp)
        i -= 1
    all.sort()
    for res in all:
        #print res, s
        if res > s:
            return res
lines = sys.stdin.readlines()
#lines = """1
#802795""".split("\n")
cn = 0
for l in lines[1:]:
    cn += 1
    print "Case #%d: %s" % (cn, func(l.strip()))

