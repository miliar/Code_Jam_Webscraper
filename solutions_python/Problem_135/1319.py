import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        answer1 = int(f.readline())
        
        for i in xrange(4):
            curr = f.readline().strip().split()
            if i + 1 == answer1:
                row1 = curr
            
        answer2 = int(f.readline())
        
        for i in xrange(4):
            curr = f.readline().strip().split()
            if i + 1 == answer2:
                row2 = curr
                
        count = 0
        found = None
        for i in xrange(4):
            if row1[i] in row2:
                count += 1
                found = row1[i]
                
        if count == 0:
            s = "Volunteer cheated!"
        elif count == 1:
            s = found
        else:
            s = "Bad magician!"
            
        print "Case #%d: %s" % (caseno+1, s)
        
main()