__author__ = 'MRajendran'
class DeceitfulWar:
    def readInput(self,f):
        f.readline()
        self.Naomi = [float(x) for x in f.readline().split()]
        self.Ken = [float(x) for x in f.readline().split()]

    def result(self):
        gameLength = len(self.Naomi)

        nWarPts = 0
        n = sorted(self.Naomi)
        k = sorted(self.Ken)
        for i in range(gameLength-1):
            nPlay = n[0]
            del(n[0])
            kIndex = 0
            for (i,p) in enumerate(k):
                if p > nPlay:
                    kIndex = i
                    break
            kPlay = k[kIndex]
            del(k[kIndex])
            if nPlay > kPlay:
                nWarPts += 1
        if n[0] > k[0]:
            nWarPts += 1

        dWarPts = 0
        n = sorted(self.Naomi)
        k = sorted(self.Ken)
        for i in range(gameLength-1):
            kAim = k[0]
            nIndex = -1
            for (i,p) in  enumerate(n):
                if p > kAim:
                    nIndex = i
                    break
            if nIndex == -1:
                nPlay = (k[-1] + k[-2])/2.0
                nIndex = 0
            else:
                nPlay = (k[-1] + 1.0)/2.0
            nReal = n[nIndex]
            del(n[nIndex])
            kIndex = 0
            for (i,p) in enumerate(k):
                if p > nPlay:
                    kIndex = i
                    break
            kPlay = k[kIndex]
            del(k[kIndex])
            if nReal > kPlay:
                dWarPts += 1
        if n[0] > k[0]:
            dWarPts += 1

        return (dWarPts, nWarPts)

d = DeceitfulWar()
fi = 'large'
f = open(fi +'.in')
o = open(fi + '.out','w')
cases = int(f.readline())
result = []

for i in range(cases):
    d.readInput(f)
    result.append(d.result())

index = 1
for r in result:
    o.write("Case #{0}: {1} {2}\n".format(index,r[0],r[1]))
    index += 1