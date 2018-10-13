# usage : wire.py problem_instance.in

import sys

sys.setrecursionlimit(3000)

def clean(s):
    if s[len(s)-1:]=='\n':
        return s[0:len(s)-1]

class Wire:

    def __init__(self,argv):
        self.argv = argv
        self.number = 0
        self.case = 0
        self.out = ''
        self.wires = []
        self.inter = 0
        self.input()

    def input(self):
        f = open(self.argv,'r')
        self.lines = f.readlines()
        f.close()
        self.number = int(self.lines[0])
        self.lines = self.lines[1:]

    def output(self):
        sys.stdout.write(self.out)
        file = self.argv.split('.in')[0]+'.out'
        f = open(file,'w')
        f.writelines(self.out)
        f.close()

    def do(self):
        self.wires = []
        self.inter = 0
        self.numberWires = int(self.lines[0])
        self.lines = self.lines[1:]
        self.doWire(self.numberWires)

    def doWire(self, n):
        if (n==0) :
            return
        self.wires.append(clean(self.lines[0]).split(' '))
        self.lines = self.lines[1:]
        self.inter += self.countInter(0, len(self.wires)-1)
        self.doWire(n-1)

    def countInter(self, n, m):
        if (n==m) :
            return 0
        if self.isInter(int(self.wires[n][0]), int(self.wires[n][1]), int(self.wires[m][0]), int(self.wires[m][1])) :
            return 1+self.countInter(n+1, m)
        else :
            return self.countInter(n+1, m)

    def isInter(self, a1, b1, a2, b2):
        return (a1<a2 and b1>b2) or (a1>a2 and b1<b2)
    
    def Run(self):
        for i in range(0, self.number):
            self.do()
            self.case += 1
            self.out += 'Case #'+str(self.case)+': '+str(self.inter)+'\n'
        self.output()

if __name__ == "__main__":
    import sys
    file = Wire(sys.argv[1])
    file.Run()
    sys.exit(0)
