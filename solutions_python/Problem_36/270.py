welcome = 'welcome to code jam'

def sup(l,t):
    r = []
    for x in l:
        if x > t:
            r.append(x)
    return r

def ind(u,v):
    first = []
    for i in range(len(u)):
        if u[i] == v:
             first.append(i)
    return first

def fill(k):
    n = len(str(k))
    return '0'*(4-n)+str(k)

def clean(s):
    if s[len(s)-1:]=='\n':
        return s[0:len(s)-1]

class WTCJ:

    def __init__(self,argv):
        self.argv = argv
        self.cases = 0
        self.case = 0
        self.wtcj = 'welcome to code jam'
        self.dict = {}
        self.res = {}
        self.input()

    def input(self):
        f = open(self.argv,'r')
        self.lines = f.readlines()
        f.close()
        self.cases = int(self.lines[0])
        self.lines = self.lines[1:]

    def output(self):
        s = ''
        for h, k in self.res.iteritems():
            s += 'Case #%s: %s\n' % (h, fill(k))                
        sys.stdout.write(s)
        file = self.argv.split('.in')[0]+'.out'
        f = open(file,'w')
        f.writelines(s)
        f.close()

    def nexttext(self):
        self.occ = 0
        self.text = clean(self.lines[0])
        self.lines = self.lines[1:]
        self.case += 1

    def occur(self,rem):
        for i in range(len(self.wtcj)):
            self.dict[i] = ind(rem,self.wtcj[i])
        self.count(-1,0)
        self.res[self.case] = fill(self.occ)

    def count(self,t,i):
        if i == len(self.dict)-1:
            self.occ += len(sup(self.dict[i],t))
        else:
            r = sup(self.dict[i],t)
            for x in r:
                self.count(x,i+1)
                
    def Run(self):
        for i in range(1,self.cases+1):
            self.res[i] = 0
            self.nexttext()
            self.occur(self.text)
        self.output()

if __name__ == "__main__":
    import sys
    wtcj = WTCJ(sys.argv[1])
    wtcj.Run()
    sys.exit(0)
