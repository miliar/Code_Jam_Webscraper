fin = open("qb.in", 'r')
fout = open("qb.out", 'w')

t = int(fin.readline())
for i in range(1, t+1):
        tmp = map(int, fin.readline().split(" "))
        n = tmp[0]
        s = tmp[1]
        passed = 0
        possible = 0
        bar = tmp[2]
        for k in range(1, n+1):
                g = tmp[2+k]
                #print g, g / 3, g % 3, g / 3 - bar 
                if g / 3 >= bar or (g % 3 == 2 and g / 3 - bar == -1):
                        passed += 1
                        #print "passed"
                elif g!=0 and g % 3 == 0 and g / 3  - bar == -1:
                        possible += 1
                        #print "possible"
                elif g % 3 == 1 and g / 3 - bar == -1:
                        passed += 1
                        #print "passed"
                elif g % 3 == 2 and g /3 - bar == -2:
                        possible += 1
                        #print "possible"

        #print passed, possible, s
        if possible >= s:
                passed += s
        else:
                passed += possible
                
        fout.write("Case #%d: %d\n" % (i, passed))
        
fout.close()
