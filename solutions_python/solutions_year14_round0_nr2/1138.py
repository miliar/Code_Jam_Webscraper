__author__ = 'MRajendran'
class cookieClicker:
    def readInput(self,f):
        s = f.readline().strip()
        self.C = float(s.split()[0])
        self.F = float(s.split()[1])
        self.X = float(s.split()[2])

    def result(self):
        currentRate = 2.0
        if self.X <= self.C:
            return self.X / currentRate
        timeSpent = self.C / currentRate
        while True:
            buyTime = self.X / (currentRate + self.F)
            noBuyTime = (self.X - self.C) / currentRate

            if noBuyTime < buyTime:
                return timeSpent + noBuyTime

            currentRate += self.F
            timeSpent += (self.C / currentRate)

c = cookieClicker()
fi = 'large'
f = open(fi +'.in')
o = open(fi + '.out','w')
cases = int(f.readline())
result = []

for i in range(cases):
    c.readInput(f)
    result.append(c.result())

index = 1
for r in result:
    o.write("Case #{0}: {1}\n".format(index,r))
    index += 1