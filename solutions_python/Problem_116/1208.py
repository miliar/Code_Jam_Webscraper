import sys

class Case :
    def __init__(self, l) :
        self.lines = l

    def match_row(self, r, ch):
        for c in range(0,4) :
            if(self.lines[r][c] != ch and self.lines[r][c] != 'T' ) :
                return False            
        return True
    def match_col(self, c, ch):
        for r in range(0,4) :
            if(self.lines[r][c] != ch and self.lines[r][c] != 'T' ) :
                return False            
        return True
    def match_diag_1(self, ch):
        for r in range(0,4) :
            if(self.lines[r][r] != ch and self.lines[r][r] != 'T' ) :
                return False
        return True
    def match_diag_2(self, ch):
        for r in range(0,4) :
            if(self.lines[r][3-r] != ch and self.lines[r][3-r] != 'T' ) :
                return False
        return True
    def check_filled(self):
        for r in range(0,4) :
            for c in range(0,4) :
                if(self.lines[r][c] == '.' ) :
                    return False       
        return True
    def find_4(self, ch):
        for i in range(0,4) :
            if(self.match_row(i,ch)) : return True;
            if(self.match_col(i,ch)) : return True;
        if(self.match_diag_1(ch)) : return True;
        if(self.match_diag_2(ch)) : return True;
        return False
    def GetResult(self) :
        x_won = self.find_4('X')
        o_won = self.find_4('O')
        if(x_won) : return "X won"
        if(o_won) : return "O won"
        if(self.check_filled()) :
            return "Draw"
        else :
            return "Game has not completed"
            
    def Solve(self, idx, fout) : 
        fout.write("Case #%d: %s\n" % (idx,self.GetResult()))        
                   
#fin = open("A-small-practice.in")
fin = open(sys.argv[1])
lines = fin.readlines()
T = int(lines[0])
fout = open(sys.argv[1][:-2] + "out","w")
cnt = 1
for i in range(1,T+1) :
    c = Case(lines[cnt:cnt+5])
    c.Solve(i,fout)    
    cnt = cnt+5
fout.close()