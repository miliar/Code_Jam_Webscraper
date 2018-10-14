# NextNumber
#
# To run this on an input file called sample.in, use the following
# command line:
#
# python base.py sample.in
#
# The output will appear on the console.  I used Python 2.5.2.
import sys

if len( sys.argv ) < 2:
    print "Please provide input file."
    exit(1)

fp = open( sys.argv[1], 'rb' )
cases = int( fp.readline() )

for case in xrange( cases ):
    line = fp.readline().strip()
    chars = {}
    base = 0
    first = True
    zeroed = False
    for ch in line:
        #print "Character %s, chars %s" % (ch, chars)
        if ch not in chars:
            if not zeroed and not first:
                zeroed = True
                chars[ch] = 0
            else:
                base += 1
                chars[ch] = base
            
        first = False
            
    if zeroed:
        base += 1
    if base < 2:
        base = 2
    
    #print "Base: %d" % base
        
    # Calculate number
    num = 0
    for ch in line:
        num *= base
        num += chars[ ch ]
        
    print "Case #%d: %d" % ( case + 1, num )