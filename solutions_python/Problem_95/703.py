'''
@author: justin lewis
'''

class Solve:
    
    t = {   ' ' : ' ' ,
            'a' : 'y' ,
            'b' : 'h' ,
            'c' : 'e' ,
            'd' : 's' ,
            'e' : 'o' ,
            'f' : 'c' ,
            'g' : 'v' ,
            'h' : 'x' ,
            'i' : 'd' , 
            'j' : 'u' ,
            'k' : 'i' ,
            'l' : 'g' ,
            'm' : 'l' ,
            'n' : 'b' ,
            'o' : 'k' ,
            'p' : 'r' ,
            'q' : 'z' ,
            'r' : 't' ,
            's' : 'n' ,
            't' : 'w' ,
            'u' : 'j' ,
            'v' : 'p' ,
            'w' : 'f' ,
            'x' : 'm' ,
            'y' : 'a' ,
            'z' : 'q' ,
        }
    
    def __init__(self,charsequence):
        self.c = charsequence
        self.o = ""        
        
        for x in charsequence:
            if x not in Solve.t:
                self.o += "_"
            else :
                self.o += Solve.t[x]                
                
        
    def to_english(self):
        return self.o
    
    
f = open("input.txt","r")
n = f.readline()

for i in range(int(n)):
    solve = Solve(f.readline().rstrip())
    print ("Case #" + str(i+1) + ": " + str(solve.to_english()))