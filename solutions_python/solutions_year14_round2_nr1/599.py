import sys
import numpy as np

def clean(s):
    latest=''
    cleanS = ''
    for c in s:
        if latest is c:
            continue
        latest = c
        cleanS += latest
    return cleanS

def interpolate(strs, cleanStr):
    hist = np.zeros(len(cleanStr))
    allHists=[]
    for s in strs:
        latest = 0        
        sHist = []
        for c in cleanStr:
            counter = 0
            for i in range(latest, len(s)):
                latest = i
                if s[i]==c:
                    counter+=1
                else:
                    break
            sHist.append(counter)
        allHists.append(sHist)

    l=len(cleanStr)
    for h in allHists:
        for i in range(l):
            hist[i] += h[i]

    hist = map(lambda x: int(round(x/len(strs))), hist)

    dist = 0
    for h in allHists:
        for i in range(l):
            dist += abs(h[i]-hist[i])

    return dist

def main():    
    tcs = int(sys.stdin.readline())
    for i in range(1, tcs+1):
        nstrs = int(sys.stdin.readline())
        strs = []
        for j in range(nstrs):
            s = sys.stdin.readline().strip()
            doable = True
            if not doable:
                continue
            tmp = clean(s)
            if j==0 :
                cleanStr = tmp
            if cleanStr != tmp:
                doable = False
            strs.append(s)    
    
        if doable:
            #print strs, cleanStr
            dist = interpolate(strs, cleanStr)
            print "Case #" + str(i) + ": " + str(dist)                        
            #hist = np.zeros()
        else:
            print "Case #" + str(i) + ": " + "Fegla Won" 
        





if  __name__ =='__main__':main()
