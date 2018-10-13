import sys
import math

def palindrome(s):
    first_half = s[0:len(s)/2]
    return s.endswith( first_half )


def solve(hi, lo):

    fairsquares = 0
#    print "%d -> %d" % (lo, hi)

    for x in xrange(lo,hi+1):
#        print "x: %d" % (x)

        if not palindrome( str(x) ):
            continue;

        val = x*x
       
        if palindrome( str(val) ):
#            print "found: %s" % (val)
            fairsquares += 1

    return fairsquares


fd = open( sys.argv[1] )

# chuck case number
fd.readline()

lines = fd.readlines()
case = 1

for line in lines:
    nums = line.rstrip().split(' ')    
    
    lo = math.ceil(math.sqrt(float(nums[0])))
    hi = math.floor(math.sqrt(float(nums[1])))

#    print "hi:",hi," lo:",lo

    # just in case...
    if( max(hi,lo) == lo ):
        (hi,lo) = (lo,hi)

    answer = solve( int(hi), int(lo) )
    print "Case #%d: %d" % (case, answer)

    case += 1

fd.close()

