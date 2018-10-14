import sys

if __name__ == "__main__":
    f = sys.stdin
    
    t = int(f.readline())
    
    for i in xrange(t):
        before = int(f.readline())
        mat1 = {}
        for k in xrange(4):
            r = f.readline().strip().split(" ")
            mat1[k + 1] = r
        after = int(f.readline())
        mat2 = {}
        for k in xrange(4):
            r = f.readline().strip().split(" ")
            mat2[k + 1] = r

        lb = mat1[before]
        cnt = 0
        item = ""
        for e in lb:
            if e in mat2[after]:
                item = e
                cnt += 1
        if cnt == 0:
            print "Case #%d: Volunteer cheated!" % (i+1)
        elif cnt > 1:
            print "Case #%d: Bad magician!" % (i+1)
        elif cnt == 1:
            print "Case #%d: %s" % (i+1,item)
            
            
            
                
        
