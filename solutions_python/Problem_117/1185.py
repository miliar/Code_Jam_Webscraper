import sys
import collections

class Case :
    def __init__(self, R,C, rows) :
        self.R = R
        self.C = C
        self.rows = rows
    def check_x(self,r,c):
        val = rows[r][c]
        for x in range(0,C) : 
            if val < rows[r][x] : 
                return False;
        return True;
    def check_y(self,r,c):
        val = rows[r][c]
        for y in range(0,R) : 
            if val < rows[y][c] : 
                return False;
        return True;
    def GetResult(self) :
        
        for r in range(0,self.R) :
            for c in range(0,self.C) :
                if(False == self.check_x(r,c)  and  False == self.check_y(r,c)) :
                    return "NO" 
        return "YES"            
        #return str(R) + " " + str(C)
    def Solve(self, idx, fout) : 
        fout.write("Case #%d: %s\n" % (idx,self.GetResult()))        
                   
#fin = open("A-small-practice.in")
fin = open(sys.argv[1])
lines = collections.deque(fin.readlines())
T = int(lines.popleft())
fout = open(sys.argv[1][:-2] + "out","w")
for i in range(1,T+1) :
    (R,C) = map(int, lines.popleft().split())
    rows = []
    for r in range(0,R) : 
        rows.append(map(int,lines.popleft().split()))
    c = Case(R,C, rows)
    c.Solve(i,fout)    
fout.close()