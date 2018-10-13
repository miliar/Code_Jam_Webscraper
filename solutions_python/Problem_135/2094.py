'''
Created on 12 Apr 2014

@author: rich
'''

def magicTrick(pathin,pathout):
    # first line is t
    
    fi = open(pathin,"r")
    fo = open(pathout,"w")
    
    t = int(fi.readline())
    
    for i in range(t):
        x1 = int(fi.readline()) 
        
        row1 = []        
        for j in range(4):
            s = fi.readline()
            if (j+1) == x1:
                row1 = (int(x) for x in s.split(' '))
            
        x2 = int(fi.readline())
        row2 = []
        for j in range(4):
            s = fi.readline()
            if (j+1) == x2:
                row2 = (int(x) for x in s.split(' '))
        
        x = list(set(row1) & set(row2))
        
        result = "Case #" + str(i+1) + ": "
        
        n = len(x)
        if n == 0:
            result += "Volunteer cheated!"
        elif n > 1:
            result += "Bad magician!"
        elif n == 1:
            result += str(x[0])
        
        result += "\n"
        fo.write(result)

if __name__ == '__main__':
    
    magicTrick("c:/rich_work/codejam2014/A-small-attempt0.in","c:/rich_work/codejam2014/magictrick.op")