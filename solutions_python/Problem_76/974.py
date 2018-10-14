'''
Created on May 7, 2011

@author: jonathanbona
'''

def parseInput(fname):
    f = open(fname,'r');
    of = open(fname+'out','w')
    
    num = int(f.readline().strip());
    
    print "Processing ",num," cases"
    
    # for each case
    for i in range(1,num+1):
        print "case ", i
        num = int(f.readline().strip())
        candies = []
        for c in f.readline().strip().split():
            candies.append(int(c))
        case =handlecase(candies)
        of.write("Case #"+str(i)+": "+case+"\n");

def lxor(list):
    result = 0
    for e in list:
        result = result ^ e
    return result

def subset(set, mask):
    result = []
    for i in set:
        if mask & 1:
            result.append(i)
        mask = mask >> 1
    return result
            

def sum(list):
    result = 0;
    for e in list:
        result = result + e
    return result

def bin(n):
     return n > 0 and bin(n >> 1)+str(n&1) or ''


def handlecase(candies):
        

    all = 2**len(candies)-1
    
    greatest = 0
    
    # produces all subsets
    for i in range(1,all):
        #print bin(i)
        
        s1 = subset(candies,i)
        s2 = subset(candies,i^all)
        if lxor(s1) == lxor(s2):
            sum1 = sum(s1)
            sum2 = sum(s2)
            greater =  sum1 if sum1 > sum2 else sum2 
            if greater > greatest:
                greatest = greater

    return str(greatest) if greatest > 0 else  "NO"
        
if __name__ == '__main__':


    parseInput('C-small-attempt0.in')

  
    
    pass