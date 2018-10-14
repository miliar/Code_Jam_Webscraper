
    
if __name__ == '__main__':
    fin = 'B-small.in'
    fon = 'B-small.out'
    
    fi = open(fin, 'r')
    fo = open(fon, 'w')
    
    c = int(fi.readline())
    for i in xrange(c):
        n, k, b, t  = [int(x) for x in fi.readline().split()]
        pi = [int(x) for x in fi.readline().split()]
        vi = [int(x) for x in fi.readline().split()]
        size = len(pi)
        passable = [pi[x] + t*vi[x] >= b for x in xrange(size)]
        
        max_pass = len(filter(lambda x: x, passable))
        
        if max_pass >= k:
            # possible
            cn = max_pass - k
            for x in xrange(size):
                if passable[x] and cn > 0:
                    passable[x] = False
                    cn -= 1
                if cn == 0:
                    break;
            count = 0
            total_lifted = 0
            for x in xrange(size):
                if passable[x]: count += 1
                else: total_lifted += count
            fo.write("Case #%d: %d\n" % (i+1,total_lifted))
        else:
            # impossible
            fo.write("Case #%d: IMPOSSIBLE\n" % (i+1))

    print "Done!"
    fi.close()
    fo.close()

