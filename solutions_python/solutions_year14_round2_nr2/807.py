'''
Created on 03.05.2014

@author: Johann
'''
'''
Created on 12.04.2014

@author: Johann
'''

with open("input.txt", "rb") as aFile:
    with open("output.txt","wb") as outFile:
        testCases=int(aFile.readline())
        #print testCases
        for case in xrange(testCases):
            A,B,K=map(int,aFile.readline().split())
            catalina=range(K)
            win=0
            win=sum([1 for a in xrange(A) for b in xrange(B) if (a&b) in catalina])
                      
            outFile.write('Case #%d: %d\n'%(case+1,win))        
            print 'Case #%d: %d'%(case+1,win)