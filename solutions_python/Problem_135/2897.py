'''
Created on 12.04.2014

@author: Johann
'''

with open("A-small-attempt0.in", "rb") as aFile:
    testCases=int(aFile.readline())
    #print testCases
    for case in xrange(testCases):
        pick1=int(aFile.readline())
        #test=map(int,[aFile.readline().split() for _ in range(4)][pick1-1])
        #print test
        row1 = set(map(int,[aFile.readline().split() for _ in range(4)][pick1-1]))
        
        pick2=int(aFile.readline())
        row2 = set(map(int,[aFile.readline().split() for _ in range(4)][pick2-1]))
        intersection=row1 & row2
        print 'Case #%d:'%(case+1),
        if len(intersection)==0:
            print 'Volunteer cheated!'
        elif len(intersection)==1:
            print intersection.pop()
        else:
            print 'Bad magician!'
            
        