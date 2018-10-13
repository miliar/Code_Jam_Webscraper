def clean(s):
    if s[len(s)-1:]=='\n':
        return s[0:len(s)-1]
    else:
        return s

def match(w,d):
    dicto = {}
    for x in range(0,10):
        dicto[x] = 0
    for x in w:
        dicto[int(x)] += 1
    dicto[0] = d[0]
    return dicto == d

class Num:
    def __init__(self,argv):
        self.argv = argv
        self.cases = 0
        self.case = 0
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
            s += 'Case #%s: %s\n' % (h, k)                
        sys.stdout.write(s)
        file = self.argv.split('.in')[0]+'.out'
        f = open(file,'w')
        f.writelines(s)
        f.close()

    def parse(self):
        self.n = clean(self.lines[0])
        self.lines = self.lines[1:]
        self.dict = {}
        for x in range(0,10):
            self.dict[x] = 0
        for l in self.n:
            self.dict[int(l)] += 1
        self.next = str(int(self.n)+1)
        self.case += 1

    def solve(self):
        while not match(self.next,self.dict):
            self.next = str(int(self.next)+1)
        self.res[self.case] = self.next
    
    def Run(self):
        for i in range(1,self.cases+1):
            self.parse()
            self.solve()
        self.output()

if __name__ == "__main__":
    import sys
    n = Num(sys.argv[1])
    n.Run()
    sys.exit(0)
