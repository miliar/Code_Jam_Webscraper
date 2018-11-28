import sys

def findDownhill(altitudes,r,c):
    rmax=len(altitudes)-1
    cmax=len(altitudes[0])-1
    v=altitudes[r][c]
    r=(r,c)
    if r<len(altitudes):
        v2=altitudes[r-1][c]
        if v2<v:
            v

class Calculator:
    def __init__(self,H,W):
        self.altitudes=[]
        self.flowTo=[]
        self.chains=[] 
        self.H=H
        self.W=W
        self.rmin=0
        self.cmin=0
        self.rmax=H-1
        self.cmax=W-1

    def addAltitudes(self,row):
        self.altitudes.append(row)

    def compareAltitudes(self,val1,coord1,coord2):
        val2=self.altitudes[coord2[0]][coord2[1]]
        if val2<val1:
            val1=val2
            coord1=coord2
        return (val1,coord1)

    def findFlowTo(self,r,c):
        coord1=(r,c)
        val1=self.altitudes[coord1[0]][coord1[1]]
        if r>self.rmin:
            (val1,coord1)=self.compareAltitudes(val1,coord1,(r-1,c))
        if c>self.cmin:
            (val1,coord1)=self.compareAltitudes(val1,coord1,(r,c-1))
        if c<self.cmax:
            (val1,coord1)=self.compareAltitudes(val1,coord1,(r,c+1))
        if r<self.rmax:
            (val1,coord1)=self.compareAltitudes(val1,coord1,(r+1,c))

        return coord1

    def findAllFlowTo(self):
        for r in range(self.H):
            row=[]
            for c in range(self.W):
                row.append(self.findFlowTo(r,c))
            self.flowTo.append(row)

    def recursiveFlow(self,r1,c1):
        (r2,c2)=self.flowTo[r1][c1]
        if r1!=r2 or c1!=c2:
            self.flowTo[r1][c1]=self.recursiveFlow(r2,c2)
        return self.flowTo[r1][c1]

    def findChains(self):
        for r in range(self.H):
            for c in range(self.W):
                self.recursiveFlow(r,c)
                    
    def dumpChains(self,output):
        letter=[chr(ord('a')+x)for x in range(26)]
        chains={}
        for r in range(self.H):
            for c in range(self.W):
                coord=self.flowTo[r][c]
                if chains.has_key(coord):
                    output.write(chains[coord])
                else:
                    x=letter[len(chains)]
                    chains[coord]=x
                    output.write(x)
                if c<self.cmax:
                    output.write(" ")
                
            output.write("\n")


input=open("B-large.in","r")
dimension=input.readline().strip().split()
T=int(dimension[0])

output=open("B-large.out","w")

for i in range(1,T+1):
    print("Case %d of %d"%(i,T))
    output.write("Case #%d:\n"%i)
    dimension=input.readline().strip().split()
    (H,W)=(int(dimension[0]),int(dimension[1]))
    calc=Calculator(H,W)
    for r in range(H):
        row=[int(x) for x in input.readline().strip().split()]
        calc.addAltitudes(row);

    calc.findAllFlowTo()
    calc.findChains()
    calc.dumpChains(output)
        

input.close()
output.close()
print "finished"