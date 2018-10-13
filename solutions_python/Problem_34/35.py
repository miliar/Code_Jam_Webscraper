from StringIO import StringIO
import re

sample = StringIO("""3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc""")

def split_testcase(testcase):
    return [x.strip("()") for x in re.findall( "\(.*?\)|.", testcase )]

def calculate(sample):
    L, D, N = [int(x) for x in sample.readline().split()]
    
    words = set()
    for i in range(D):
        words.add( sample.readline().strip() )
        
    print words
    
    testcases = []
    for i in range(N):
        testcases.append( sample.readline().strip() )
        
    for j, testcase in enumerate(testcases):
        #print "test case", j+1
        
        pieces =  split_testcase(testcase)
        
        remainder = words
        for i, piece in enumerate( pieces ):
            remainder = [word for word in remainder if word[i] in piece]
            
        print "Case #%d: %d"%(j+1, len(remainder))
                
            
    
if __name__=='__main__':
    fp = open( "A-large.in" )
    calculate( fp )
    print "done"