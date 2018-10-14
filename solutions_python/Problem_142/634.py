import sys, math
from itertools import groupby
import difflib

def main():
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        f = open(file)
        numOfTest = f.readline().split()[0]
        for k in range(int(numOfTest)):
            Nums = int(f.readline().split()[0])
            at = ''
            li = []
            flag = False
            for i in range(Nums):
                a = f.readline().split()[0]
                li.append(a)
                stri = strippin(a)
                if at == '':
                    at = stri
                else:
                    if at != stri:
                        print "Case #" + str(k+1) + ": " + "Fegla Won"
                        flag = True
                        continue
            res = distanceSmall(li, at)
            if not flag:        
                print "Case #" + str(k+1) + ": " + str(res)
            
def strippin(li):
    a = [x[0] for x in groupby(li)]
    return ''.join(a)
    
def distanceSmall(li, a):
    word1 = li[0]
    word2 = li[1]
    
    lendiff = 0
    index1 = 0
    index2 = 0
    for char in a:
        sub1 = 0
        sub2 = 0
        while index1 < len(word1) and word1[index1] == char :
            index1 +=1
            sub1 +=1
        while index2 < len(word2) and word2[index2] == char  :
            index2 +=1
            sub2 +=1
        lendiff += abs(sub1 - sub2)
    return lendiff
    
if __name__ == '__main__':
    main()