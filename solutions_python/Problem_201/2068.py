
class Stall:

    def __init__(self,position):
        self.pos = position
        self.occupied = False
        self.ls = 0
        self.rs = 0        
    def max(self):
        if self.occupied == True:
            return 0
        return max([self.ls,self.rs])
    
    def min(self):
        if self.occupied ==True:
            return 0
        return min([self.ls,self.rs])
    
    def show(self):
        if self.occupied == True:
            print('x',end='')
        else:
            print('o',end='')
    
def resetLsRsFromPos(stalls, pos,side):
    if side == 'ls' or side == 'both':
        for i in range(pos+1,n+1):
            if stalls[i].occupied == True:
                break
            else:
                stalls[i].ls = i-pos
            
    if side == 'rs' or side == 'both':
        for i in range(pos-1,0,-1):
            if stalls[i].occupied == True:
                break
            else:
                stalls[i].rs = pos-i
            
        
        
def solve(n,k):
    stalls = []
    for i in range(0,n+2):
        stall = Stall(i)
        if i==0 or i==n+1:
            stall.occupied = True
        stalls.append(stall)
    
    resetLsRsFromPos(stalls,0,'ls')
    resetLsRsFromPos(stalls,n+1,'rs')
    
    
    for i in range(0,k):
        totalMax = 0
        totalMin = 0
        
        for stall in stalls:
            if stall.min() > totalMin:
                totalMin = stall.min()
                totalMax = stall.max()
                pos = stall.pos
            if stall.min() == totalMin and stall.max() > totalMax:
                totalMax = stall.max()
                pos = stall.pos
                
        stalls[pos].occupied = True
        resetLsRsFromPos(stalls,pos,'both')
        #for stall in stalls:
            #stall.show()
        #print('')
                
    return totalMax-1,totalMin-1

    
    
    
    

#fin = open("input.txt", "r")
fin = open("C-small-1-attempt0.in","r")
#fin = open("B-large.in","r")
fout = open("output.txt","w")

tFile = fin.readlines()
t = int(tFile.pop(0).strip('\n'))


for numLine in range(0,t):
    line = tFile.pop(0).strip('\n').split(' ')

    n = int(line[0])
    k = int(line[1])
    
    
    
    y,z = solve(n,k)
        
        

    print("Case #" + str(numLine+1) + ': ', end='')
    print("Case #" + str(numLine+1) + ': ', end='', file=fout)
    
    print(str(y) + ' ' + str(z))
    print(str(y) + ' ' + str(z), file=fout)


fout.close()
fin.close()
