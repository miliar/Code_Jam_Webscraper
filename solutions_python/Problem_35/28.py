class Basin(object):
    def __init__(self,elevation):
        self.parent = self
        self.label = None
        self.elevation = elevation
        self.n = None
        self.s = None
        self.e = None
        self.w = None
    def __str__(self):
        return self.getLabel()
    def sink(self):
        return self.parent == self
    def findSink(self):
        if self.sink(): return self
        sink = self.parent.findSink()
        self.parent = sink
        return sink
    def setLabel(self,label):
        self.findSink().label = label
    def getLabel(self):
        return self.findSink().label
    def labeled(self):
        return self.getLabel() != None
    def flow(self):
        min = self.elevation
        for basin in (self.n,self.w,self.e,self.s):
            if basin and basin.elevation < min:
                min = basin.elevation
                self.parent = basin

t = int(raw_input())
for i in xrange(t):
    h,w = (int(j) for j in raw_input().split())
    watershed = []
    for j in xrange(h):
        watershed.append([Basin(int(k)) for k in raw_input().split()])
    for j in xrange(1,h):
        for k in xrange(w):
            watershed[j][k].n = watershed[j-1][k]
    for j in xrange(h-1):
        for k in xrange(w):
            watershed[j][k].s = watershed[j+1][k]
    for k in xrange(1,w):
        for j in xrange(h):
            watershed[j][k].w = watershed[j][k-1]
    for k in xrange(w-1):
        for j in xrange(h):
            watershed[j][k].e = watershed[j][k+1]

    for row in watershed:
        for basin in row:
            basin.flow()

    print "Case #%d:"%(i+1)

    labels = "abcdefghijklmnopqrstuvwxyz"
    index = 0
    for row in watershed:
        for basin in row:
            if not basin.labeled():
                basin.setLabel(labels[index])
                index += 1
        print " ".join(str(b) for b in row)
