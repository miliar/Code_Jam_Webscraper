'''
@author: justin lewis
'''

class Solve:
    
    def __init__(self,charsequence):
        
        splitstr = charsequence.split()
        
        self.n = int(splitstr[0])      # number of googlers
        self.s = int(splitstr[1])      # number of surprising triplicates of scores
        self.p = int(splitstr[2])      # min score
        
        can = 0
        canWithSurprise = 0
        
        for i in range(self.n):
            total = int(splitstr[i+3])
            
            low = self.p + (max(0,self.p-1))*2
            lows = self.p + (max(0,self.p-2))*2
            
            if(total >= low):
                can += 1
            elif(total >= lows):
                canWithSurprise += 1
        
        self.m = can + min(self.s, canWithSurprise)
        
    def max_googlers(self):
        return self.m
    
class Score:
    
    def __init__(self, total, minscore):
        
        self.t = total
        self.s = minscore
        self.hm = ((minscore * 3 - 2) <= total)
        self.hmus = ((minscore * 3 - 4) <= total)
        
        if(total == 0):
            self.hm = False
            self.hmus = False
        elif(total == 1):
            self.hmus = False
        
    def has_minimum(self):
        return self.hm
    
    def has_minimum_using_surprise(self):
        return self.hmus
    
    
f = open("input.txt","r")
o = open('output.txt', "w")
n = f.readline()

for i in range(int(n)):
    solve = Solve(f.readline().rstrip())
    val = str(solve.max_googlers())
    print ("Case #" + str(i+1) + ": " + val)
    print ("Case #" + str(i+1) + ": " + val, file=o)
    