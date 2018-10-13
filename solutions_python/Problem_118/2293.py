'''
Created on 13/apr/2013

@author: valentinarho
'''
import math;

def ispal(num):
    s = str(num);
    return ispalhelp(s)
    
def ispalhelp(s):
    l = len(s)
    if l == 1 or l == 0:
        return True
    elif s[0] == s[(l-1)]:
        return ispalhelp(s[1:(l-1)])
    else: 
        return False

def calcsquare(num):
    #deve terminare con 1, 4, 5, 6, 9
    num = str(num)
    l = len(num)
    if num[l-1] != '1' and num[l-1] != '4' and num[l-1] != '5' and num[l-1] != '6' and num[l-1] != '9':
        return -1
        
    else:
        sq = math.sqrt(int(num))
        ssq = str(sq)
        if '.' in ssq and ssq[len(ssq)-1] != '0':
            return -1
        else:
            return sq

if __name__ == '__main__':
    nomefile = "C-small-attempt0"
    
    # open file input
    input = open(nomefile+'.in','r');
    out = open(nomefile+'.out','w');
        
    # number of test case
    T = int(input.readline()); 
    
    for i in range(1,T+1): #da 1 a t
        A,B = [int(x) for x in input.readline().split()]
        count = 0
        for num in range(int(A), int(B)+1):
            if ispal(num):
                sq = calcsquare(num)
                
                if sq != -1 and ispal(int(sq)):
                    count = count+1
                    
        out.write("Case #"+str(i)+": "+str(count)+"\n");
        
        