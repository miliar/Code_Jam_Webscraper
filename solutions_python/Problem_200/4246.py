import sys
import copy
import os


class Problem(object):
    def __init__(self,strN,idx):
        self.strN = strN
        self.solution = None
        self.idx = idx
    
    def solve(self) -> int :
        self.solution = self.idx
        pass

    def tostring(self):
        return "Case #%s: %s" % (self.idx,self.solution )

class Solver0(Problem):
    def __init__(self,strN,idx):
        Problem.__init__(self,strN,idx)

    def solve(self):
        self.solution = self.getSolution(self.strN)

    def getSolution(self,strN):
        #print(strN)
        if isTidyNumber(strN):
            return strN
        if strN[0] == '0' and len(strN) > 1:
            return self.getSolution(strN[1:])
        cChar=strN[0]
        cIdx = 0
        decmp = list(map(lambda x : int(x),strN))
        for i in range(len(strN)) :
            if i + 1 < len(decmp) :
                if decmp[i] < decmp[i+1]:
                    cIdx = i+1
                    cChar = decmp[cIdx]
                if decmp[i] > decmp[i+1] :
                    decmp[cIdx] += -1
                    decmp[cIdx+1:] = [9]* ( len(decmp) - 1 - cIdx )
                    if not(decmp[0] == 0)  :
                        return ''.join(list(map(lambda x : str(x),decmp)))
                    else :
                        return ''.join(list(map(lambda x : str(x),decmp[1:])))
        return strN


    #def getSolution_old(self,strN):
    #    if isTidyNumber(strN):
    #        return N
    #    if strN[0] == 0:
    #        return 9*len()
    #    strN = str(N)
    #    decmp= getNormalDecomposition(N)
    #    for i in range(len(decmp)) :
    #        if i < len(decmp) :
    #            if decmp[i] > decmp[i+1] :
    #                decmp[i] += -1
    #                decmp[i+1:] = [9]* ( len(decmp) - 1 - i )
    #                return self.getSolution()
    #                else :
    #                    return self.getSolution(decmp)
    #                if i == 0 and decmp[i] == 1
    #                else :
    #                    '9' * ( maxBase - 1 )
    #                decmp2[i] = decmp[i+1]


def charArryToString(ca):
    """
    
    :param ca: 
    :return: 
    """
    return ''.join(ca)

def isTidyNumber(strN : str):
    """
    >>> isTidyNumber("12345")
    True
    >>> isTidyNumber("10000")
    False
    >>> isTidyNumber("234560")
    False
    >>> isTidyNumber("123454678")
    False
    >>> isTidyNumber('12345555789')
    True
    >>> isTidyNumber('7')
    True
    """
    for i in range(len(strN)):
        if i + 1 < len(strN) :
            if( int(strN[i]) > int(strN[i+1])):
                return False
    return True

def getFirstBasePower(N):
    """
    >>> getFirstBasePower(123)
    2
    >>> getFirstBasePower(25790)
    4
    """
    return len(str(N)) - 1

def getBase(N):
    return sorted(range(getFirstBasePower(N)), key= lambda  x : x,reverse=True)

def getBaseDecomposition_old(N):
    strN = str(N)
    return dict(zip( getBase(N), strN ))

def getBaseDecomposition(N):
    """
    >>> getBaseDecomposition(2579)
    [9, 7, 5, 2]
    """
    strN = str(N)
    inverseN = []
    for i in range(len(strN)):
        inverseN.append( int(strN[len(strN)-(i+1)] ) )
    return inverseN

def getNormalDecomposition(N):
    """
    >>> getNormalDecomposition(1235)
    [1, 2, 3, 5]
    """
    return list(map(lambda x : int(x), str(N)))


        


def loadProblems(inputFile):
    import doctest
    doctest.testmod()
    with open(inputFile,'r') as f :
        lines = f.read().splitlines()
        T = lines[0]
        idx = 0
        for l in lines[1:]:
            strN = l.replace(' ','')
            idx+=1
            yield Solver0(strN,idx)
    


if __name__ == '__main__' :
    if len(sys.argv) != 3 :
        print("fuck off")
        sys.exit(-1)
    infile = sys.argv[1]
    output = sys.argv[2]
    solutions = []
    o = open(output,'w')
    for p in loadProblems(infile):
        p.solve()
        o.write(p.tostring()+"\n")
    o.close()
         
