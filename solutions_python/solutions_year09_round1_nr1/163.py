import math
import sys
#import random



def next(m,b):
    result = 0;
    while m!=0:
        d = m % b
        m = m / b
        result += d*d
    return result
    
    

def doCase():
    bases = sf.readline().strip('\n').split(' ')
    numBases = len(bases)
    n=2
    while (True):
        numGoodBases = 0
        for b in bases:
            m=n
            goodBase = False
            b = int(b)
            tempSet=set()
            while (not m in mySet[b]) and (not m in tempSet):
                if m in goodSet[b]:
                    goodBase = True
                    numGoodBases += 1
                    goodSet[b] = goodSet[b].union(tempSet) # found good number, all numbers reaching it are good
                    break
                tempSet.add(m)
                m = next(m, b)
            if not goodBase:
                mySet[b] = mySet[b].union(tempSet)
                break
        if numGoodBases==numBases:
            return str(n)
        n+=1
    return "NONE"
            



def processFile(source, target):
    global sf #want to read file in all functions
    global mySet
    global goodSet
    
    mySet = [0] * 11
    goodSet = [0] * 11
    for i in range(2,11):
        goodSet[i] = set()
        goodSet[i].add(1)
        mySet[i] = set()
   
    sf = open(source)
    tf = open(target,"w")
    T = sf.readline()
    T = int(T)
    for case in range(1, T+1):
        result = doCase()
        print 'Case #' + str(case) + ': ' + result
        newline = 'Case #' + str(case) + ': ' + result
        tf.write(newline)
        if not case==T: tf.write('\n')
    sf.close
    tf.close
        
def main(argv = None):
    if argv is None:
        argv = sys.argv
    processFile("A-small-attempt1.in", "A-small-attempt1.out")
    if (len(argv)>2):
        processFile(argv[1], argv[2])
    
if __name__ == "__main__":
    main()
    