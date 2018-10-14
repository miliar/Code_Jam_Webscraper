import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline().strip())
    
    for caseno in xrange(ncases):
        nvines = int(f.readline().strip())
        
        vines = []
        for i in xrange(nvines):
            s = f.readline()
            a, b = s.split()
            vines.append((int(a), int(b)))
            
        target = int(f.readline().strip())
        
        vines.append((target, -1))
        
        res = swing(vines, 0, vines[0][0])
        
        if res:
            s = "YES"
        else:
            s = "NO"
            
        print "Case #%d: %s" % (caseno+1, s)
        
    
def swing(vines, cvine, reach):
    a = vines[cvine]
    index = cvine + 1
    while index < len(vines):
        b = vines[index]
        if (b[0] - a[0]) > reach:
            break
            
        if b[1] == -1:
            return True
            
        newreach = min(b[0] - a[0], b[1])
        
        result = swing(vines, index, newreach)
        if result:
            return True
        
        index += 1
        
    return False
    
main()