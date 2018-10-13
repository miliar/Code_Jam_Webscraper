import sys
import collections
import math

class Case :
    def __init__(self, A, B) :
        self.A = A
        self.B = B
    
    def check_pal(self,s):
        if(s == self.ReverseNumber(s)) : return True
        
        return False
    def ReverseNumber(self, n, partial=0):
        if n == 0:
            return partial
        return self.ReverseNumber( n / 10, partial * 10 + n % 10)

    def GetResult(self) :
        lower_sqrt = int(math.floor(math.sqrt(self.A)))
        upper_sqrt = int(math.ceil(math.sqrt(self.B)))
        cnt = 0;
        for s in range(lower_sqrt,upper_sqrt+1) :
            if(self.check_pal(s)) :
                s_s = s**2
                if(self.A <= s_s and s_s <= self.B) : 
                    if(self.check_pal(s_s)) :
                        cnt = cnt+1;
                           
        return cnt
    def Solve(self, idx, fout) : 
        fout.write("Case #%d: %s\n" % (idx,self.GetResult()))        
                   
#fin = open("A-small-practice.in")
fin = open(sys.argv[1])
lines = collections.deque(fin.readlines())
T = int(lines.popleft())
fout = open(sys.argv[1][:-2] + "out","w")
for i in range(1,T+1) :
    (A,B) = map(int, lines.popleft().split())
    c = Case(A,B)
    c.Solve(i,fout)    
fout.close()