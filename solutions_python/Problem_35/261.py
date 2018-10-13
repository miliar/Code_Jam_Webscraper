# usage : ws.py problem_instance.in
# solution file: problem_instance.out

class WS:

    def __init__(self,argv):
        self.argv = argv
        self.cases = 0
        self.case = 0
        self.h = 0
        self.w = 0
        self.out = ''
        self.input()

    def input(self):
        f = open(self.argv,'r')
        self.lines = f.readlines()
        f.close()
        self.cases = int(self.lines[0])
        self.lines = self.lines[1:]

    def output(self):
        sys.stdout.write(self.out)
        file = self.argv.split('.in')[0]+'.out'
        f = open(file,'w')
        f.writelines(self.out)
        f.close()

    def mapping(self):
        coords = self.lines[0].split(' ')
        self.height = int(coords[0])
        self.width = int(coords[1])
        self.lines = self.lines[1:]
        self.map = {}
        for i in range(1,self.height+1):
            for j in range(1,self.width+1):
                coords = self.lines[0].split(' ')
                self.map[i,j]=int(coords[j-1])
            self.lines = self.lines[1:]
        self.case += 1

    def inmap(self,(a,b)):
        return (a in range(1,self.height+1)) and (b in range(1,self.width+1))

    def alt(self,(a,b),(u,v)):
        return  self.map[a,b] - self.map[u,v]

    def neighbor(self):
        self.n = self.i - 1,self.j
        self.w = self.i, self.j-1
        self.e = self.i,self.j+1
        self.s = self.i + 1,self.j
        points = [
                ((self.i,self.j),True),
                (self.n,self.inmap(self.n)),
                (self.w,self.inmap(self.w)),
                (self.e,self.inmap(self.e)),
                (self.s,self.inmap(self.s)),
                  ]
        l = []
        for x in points:
            (i,j),k = x
            if k:
                l.append((i,j))
        l.sort(cmp=self.alt)
        self.f = l[0]

    def sink(self):
        self.neighbor()
        if (self.i, self.j) == self.f:
            self.sinkpoint = self.f
            self.sinks.add(self.f)
        else:
            (self.i, self.j) = self.f
            self.sink()

    def drain(self):
        self.geo = {}
        self.result = {}
        self.sinks = set([])
        for (i,j), k in self.map.iteritems():
            self.i = i
            self.j = j
            self.sink()
            self.geo[i,j] = self.sinkpoint

        l = []
        for i in range(len(self.sinks)):
            l.append(chr(i+97))
        l.sort()

        s = []
        for i in range(1,self.height+1):
            for j in range(1,self.width+1):
                try:
                    s.index(self.geo[i,j])
                except:
                    s.append(self.geo[i,j])
        l = []
        for i in range(len(self.sinks)):
            l.append(chr(i+97))
        l.sort()
            
        for (i,j), k in self.geo.iteritems():
            self.result[i,j] = l[s.index(self.geo[i,j])]          
        self.out += 'Case #%s: \n' % (self.case)
        for i in range(1,self.height+1):
            l = ''
            for j in range(1,self.width+1):
                l += str(self.result[i,j])+' '
            self.out += l+'\n'
    
    def Run(self):
        for i in range(1,self.cases+1):
            self.mapping()
            self.drain()
        self.output()

if __name__ == "__main__":
    import sys
    ws = WS(sys.argv[1])
    ws.Run()
    sys.exit(0)
