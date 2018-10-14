labellist = "abcdefghijklmnopqrstuvwxyz"

class cell:
    id = 0
    def __init__(self, alt):
        self.id = self.__class__.id
        self.__class__.id += 1
        self.alt = alt
        self.flow = None
        self.label = None
        self.N = None
        self.S = None
        self.E = None
        self.W = None
    def issink(self):
        if self.flow is None:
            self.flowdir()
        return self.flow is False
    def flowdir(self):
        if self.flow is None:
            if len([x.alt for x in (self.N, self.W, self.E, self.S) if x is not None]) == 0:
                self.flow = False
            else:
                mina = min([x.alt for x in (self.N, self.W, self.E, self.S) if x is not None])
                if mina >= self.alt:
                    self.flow = False
                elif self.N is not None and self.N.alt == mina:
                    self.flow = self.N
                elif self.W is not None and self.W.alt == mina:
                    self.flow = self.W
                elif self.E is not None and self.E.alt == mina:
                    self.flow = self.E
                elif self.S is not None and self.S.alt == mina:
                    self.flow = self.S
        return self.flow
    def getlabel(self):
        if self.label is not None:
            return self.label
        if self.issink():
            self.label = next(labels)
        elif self.flow.label is not None:
            self.label = self.flow.label
        else:
            self.label = self.flow.getlabel()
            
        return self.label
        

with open("B.in") as infile:
    with open("B.out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            H, W = [int(x) for x in infile.readline().split()]
            cmap = []
            for i in range(H):
                row = [cell(int(x)) for x in infile.readline().split()]
                cmap.append(row)
            for i in range(H):
                for j in range(W):
                    if i != 0:
                        cmap[i][j].N = cmap[i-1][j]
                    if i != H-1:
                        cmap[i][j].S = cmap[i+1][j]
                    if j != 0:
                        cmap[i][j].W = cmap[i][j-1]
                    if j != W-1:
                        cmap[i][j].E = cmap[i][j+1]
            labels = iter(labellist)
            chars = "\n".join([" ".join([c.getlabel() for c in row]) for row in cmap])
            # Perform all nessesary calculation
            outfile.write("Case #{nc}:\n{data}\n".format(nc=ncase+1,data=chars))
print("Ready")
