'''
Created on May 7, 2011

@author: Guy
'''
def processInput(inFileName,outFileName):
    f = open(inFileName)
    fo = open(outFileName,'w')
    numLines = int(f.readline().rstrip())
    for i in xrange(numLines):
        numCandies = int(f.readline().rstrip())
        candyVals = map(int,f.readline().rstrip().split())
        candyVals = candyVals[0:numCandies]
        if numCandies<2 or reduce(lambda x,y: x^y,candyVals)!=0:
            res = 'Case #'+str(i+1)+': NO'
        else:
            res = 'Case #'+str(i+1)+': ' + str(sum(candyVals)-min(candyVals))
        print res
        fo.write(res +'\n')
                
processInput('C-large.in','C-out-large.txt')