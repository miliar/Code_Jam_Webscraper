import sys
import math

def solve( r, t ):

    numcirc = 0

    r += 1

    while True:
        t -= 2*r-1        
        r += 2
        if t >= 0:
            numcirc += 1
        else:
            break;

    return numcirc



# GO!!
if __name__ == "__main__":
    fd = open( sys.argv[1] )

    # chuck case number
    fd.readline()

    lines = fd.readlines()
    case = 1

    for line in lines:
        nums = line.rstrip().split(' ')    
        
        r = int(nums[0])
        t = int(nums[1])

        answer = solve( r, t )
        print "Case #%d: %d" % (case, answer)

        case += 1

    fd.close()

