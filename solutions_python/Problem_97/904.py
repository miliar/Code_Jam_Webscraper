if __name__ == '__main__':
    for i in range(1, int(raw_input()) + 1):
        
        a, b = raw_input().split(' ')
        total = 0
#        print a, b
        
        for n in xrange(int(a), int(b)):
            n = str(n)
            previous = ''
            
            for l in xrange(1, len(n)):
                m = n[l:] + n[0:l]
                if int(m) <= int(b) and int(m) > int(n) and int(m[0]) != 0 and n.rstrip(n[l]) != '' and m != previous:
                    previous = m
                    total += 1
#                    print (n, n[l:] + n[0:l])
                    
        print "Case #" + str(i) + ": " + str(total)