#!/usr/bin/python

infile = "A-large.in"

f    = open( infile )
fout = open( infile.replace("in","out") , "w" )


T = int ( f.readline() )

def solve( digits ):

    ans = 0
    c = 0 # number of people that stand up 
    for shyness_level,n in enumerate(digits) :

        stand_up = shyness_level <= c
        needed   = shyness_level - c
        
        # print " have ",c, "people with SL <",shyness_level

        if stand_up : # ok
            pass
        else :
            # print "need", needed
            c+= needed
            ans += needed
        c+=int(n)

    return ans


for i in range( 1, T+1 ):
    
    smax, digits  = f.readline().split()
    
    # print smax, digits

    ans = solve( digits )
    
    
    print "Case #%d: %s" % (i, ans)
    fout.write( "Case #%d: %s\n" % (i, ans))

fout.close()
