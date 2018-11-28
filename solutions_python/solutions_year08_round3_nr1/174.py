#!/usr/bin/env python
#
# task 1
#
import operator

def do_trial(f):
    line = [int(x) for x in f.readline().split()]
    maxNumOfLetters = line[0]  
    keysAvaiable = line[1] 
    lettersInAlphabet = line[2]
    line = [int(x) for x in f.readline().split()]
    #v = []
    #for j in xrange(0,len(line),2):
    #        v.append( ( line[j] , line[j+1] ) )
    
    di = []
    for i in xrange( 0,lettersInAlphabet ):
        di.append( ( i , line[i] ) )

    di.sort( key=operator.itemgetter(1) , reverse=True )
        
    di2 = {}
    for i in xrange( 0 , keysAvaiable ):
        di2[i] = []
        
        
    keyonphone = 0
    for i in xrange( 0 , lettersInAlphabet ):
        key = di[ i ]
        
        list = di2[ keyonphone ]
        list.append( key[0] )
        di2[ keyonphone ] = list
           
        keyonphone = ( keyonphone + 1 ) % keysAvaiable

    di3 = {}
    for i in xrange( 0 , len( di2 ) ):
        #print i,":",
        for j in xrange( 0 , len( di2[i] ) ):
            #print j+1 , '-' , di2[i][j],
            di3[ di2[i][j] ] = j + 1 
        
        #print
    #print
    #print di2
    #print di3
    
    dsum = 0
    for litera in xrange( 0 , lettersInAlphabet ):
        ilerazywystepuje = line[litera ]
        dsum = dsum + di3[ litera ] * ilerazywystepuje
        
    return dsum
    #print di3
    #print di
    #print line
    return 0
    
#f = sys.stdin
f = open("A-large.in")
T = int(f.readline())
for i in xrange(T):
    v = do_trial(f)
    print "Case #%d: %d" % (i+1,v)