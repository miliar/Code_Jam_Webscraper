#!/usr/bin/env python

import sys

comps = {
    "11" : "1",
    "1i" : "i",
    "1j" : "j",
    "1k" : "k",
    "i1" : "i",
    "ii" : "-1",
    "ij" : "k",
    "ik" : "-j",
    "j1" : "j",
    "ji" : "-k",
    "jj" : "-1",
    "jk" : "i",
    "k1" : "k",
    "ki" : "j",
    "kj" : "-i",
    "kk" : "-1",
}


def compute(x):
    sign = "-" if x.count("-") == 1 else ""
    retval = sign + comps[x.replace("-", "")]
    if retval.startswith("--"):
        return retval[2:]
    return retval
    

def getFirst(S, letter, skip, rev = False):
    first = S[0]
    for i, s in enumerate(S[1:]):
        if ((skip and i > 0) or (not skip)) and first == letter:
            break
        #print letter +":", first + s, "= ",
        first = compute(first + s if not rev else s + first)
        #print first
    else:
        if first != letter:
            return None
        
    pos = i + 1
    if pos >= len(S):
        return None
        
    return pos

def getLast(S, skip):
    pos = getFirst("".join(reversed(S)), "k", skip, True)
    if pos is not None:
        return len(S) - pos
        
    return None
    

def multiCompute(x):
    letter = x[0]
    for s in x[1:]:
        #print "j:", letter + s, "=",
        letter = compute(letter + s)
        #print letter
    
    return letter

def solve():
    #print
    L, X = tuple(int(one) for one in sys.stdin.readline().split())
    S = sys.stdin.readline().strip() * X
    if len(S) < 3:
        return "NO"
    
    #print S
    skip = False
    while True:
        lastS = S
        
        firstPos = getFirst(S, "i", skip)
        #print "< first"
        
        if firstPos is None:
            if not skip:
                return "NO"
        else:    
            S = "i" + S[firstPos:]
        
        lastPos = getLast(S, skip)
        #print "< third"
        
        if lastPos is None:
            if not skip:
                return "NO" 
        else:
            S = S[:lastPos] + "k"
        
        if len(S) < 3:
            return "NO"
        
        if "j" == multiCompute(S[1:-1]):
            return "YES"
        else:
            if lastS == S:
                break
            
            skip = True
            
        #print "#:", S
    return "NO"


def main():
	T = int(sys.stdin.readline())
	for caseNumber in xrange(1, T+1):
	    print "Case #%d: %s" % (caseNumber, solve())


if __name__ == '__main__':
	main()

