s = "So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem \"welcome to code jam.\" After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam."
#s = "wweellccoommee to code qps jam"
t = "welcome to code jam"

f = open("codejamm.txt","r")
g = open("codeout.txt","w")

index = 0

line = f.readline()
number = int(line)

while True:
    line = f.readline()
    
    if not line:
        break

    index += 1
    s = line.strip()

    m = list()
    for x in xrange(len(s)):
        m.append(0)

    d = {}

    for x in xrange(len(s)):
        if s[x] not in d:
            d[s[x]] = list()
        d[s[x]].append(x)

    for x in xrange(len(t)):
        if t[x] not in d:
            d[t[x]] = list()
        if x == 0:
            a = d[t[x]]
            for x in xrange(len(a)):
                m[a[x]] = 1
            continue

        a = d[t[x]]
        b = d[t[x-1]]

        for ax in xrange(len(a)):
            m[a[ax]] = 0
            for bx in xrange(len(b)):
                if b[bx] < a[ax]:
                    m[a[ax]] += m[b[bx]]

        if x == len(t) - 1:
            count = 0
            a = d[t[x]]
            for stuff in a:
                count += m[stuff]

    g.write("Case #" + str(index) + ": " + '%(stuff)04d' % {'stuff' : count%10000 } + "\n")

f.close()
g.close()
