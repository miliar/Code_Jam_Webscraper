def c(s):
    if len(s) <=1:
        return 0
    else:
        pe = 0
        ac = 0
        for i in range(len(s)):
            if (pe+ac)>= i:
                pe+=int(s[i])
            else:
                ac+=(i-(pe+ac))
                pe+=int(s[i])
    return ac

res = []

n = int(raw_input())
for i in range(n):
    en = raw_input().split()[1]
    res.append(c(en))

for i in range(len(res)):
    print "Case #{0:d}: {1:d}".format(i+1,res[i])
