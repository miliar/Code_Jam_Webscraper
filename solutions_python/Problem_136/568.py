#!python2
'''
Created on Apr 11, 2014

@author: Mike
'''

import sys

def cookies(C, F, X, rate):
   
    previous = X/rate
    
    nxt = 0
    time = 0
    
    while True:
        time = time + C/rate
        rate = rate + F
        
        nxt = time + (X/rate)
        
        #print previous, nxt, rate, (previous < nxt)
        
        if (previous < nxt):
            break
        else:
            previous = nxt
    
    return previous

def openForWriting():
    from os.path import expanduser
    home = expanduser("~")
    path = home + '/git/GoogleCodeJam2014/Qualification/' + "cc1.txt"
    
    wf = open(path, 'w')
    
    return wf

def readFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '/Downloads/' + fileName 
    #print path
    f = open(path , 'r')
    
    wf = openForWriting()
    
    cases = int( f.readline() )
    
    i = 1
    while i <= cases:
        var = f.readline().rstrip('\n').split(" ")
        C = float( var[0] )
        F = float( var[1] )
        X = float( var[2] )
        #print C, F, X
        time = cookies( C, F, X, float(2))
        
        wf.write( ("Case #" + str(i) + ": " + ("%.7f" % round(time,7)) + "\n").encode('UTF-8') )
        print ("Case #" + str(i) + ": " + ("%.7f" % round(time,7)) + "\n").encode('UTF-8')
        i += 1
        
        


if __name__ == '__main__':
    fileName = sys.argv[-1]
    readFile(fileName)