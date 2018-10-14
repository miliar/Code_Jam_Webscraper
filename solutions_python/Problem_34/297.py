# usage : al2.py problem_instance.in
# solution file: problem_instance.out

def clean(s):
    if s[len(s)-1:]=='\n':
        return s[0:len(s)-1]

class AL:

    def __init__(self,argv):
        self.argv = argv
        self.i = 0
        self.l = 0
        self.d = 0
        self.dict = []
        self.res = {}
        self.letters = {}
        self.cases = 0
        self.input()

    def input(self):
        f = open(self.argv,'r')
        self.lines = f.readlines()
        f.close
        let = self.lines[0].split(' ')
        self.l = int(let[0])
        self.d = int(let[1])
        self.cases = int(let[2])
        self.lines = self.lines[1:]
        for i in range(self.d):
            self.dict.append(clean(self.lines[0]))
            self.lines = self.lines[1:]
        for i in range(1,self.l+1):
            self.letters[i] = []
            for x in self.dict:
                self.letters[i].append(x[i-1])

    def output(self):
        s = ''
        for h, k in self.res.iteritems():
            s += 'Case #%s: %s\n' % (h, k)                
        sys.stdout.write(s)
        file = self.argv.split('.in')[0]+'.out'
        f = open(file,'w')
        f.writelines(s)
        f.close()

    def word(self):
        self.s = clean(self.lines[0])
        self.lines = self.lines[1:]
        self.groups = {}
        self.f = 0
        self.par = False
        for x in self.s:
            if x == '(':
                self.par = True
                self.groups[self.f] = []
            elif x == ')':
                self.par = False
                self.f += 1
            else:
                if self.par:
                    self.groups[self.f].append(x)
                else:
                    self.groups[self.f] = x
                    self.f +=1
        self.i += 1

    def solve(self):
        t = 0
        for x in self.dict:
            test = True
            for j in range(len(x)):
                if not x[j] in self.groups[j]:
                    test = False
            if test:
                t += 1
        self.res[self.i] = t
                
    def Run(self):
        for i in range(1,self.cases+1):
            self.res[i] = 0
            self.word()
            self.solve()
        self.output()


if __name__ == "__main__":
    import sys
    al = AL(sys.argv[1])
    al.Run()
    sys.exit(0)
