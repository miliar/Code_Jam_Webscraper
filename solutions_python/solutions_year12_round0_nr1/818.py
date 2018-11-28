
def main(d):
    inpfile = open("A-small-attempt2.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()

        re = ""
        for e in line:
            
            re += d[e]
        
        
        result = "Case #" + str(case) + ": " + str(re)+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":

    #main()
    a1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    a2 = "our language is impossible to understand"
    
    b1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    b2 = "there are twenty six factorial possibilities"
    
    c1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    c2 = "so it is okay if you want to just give up"
    
    d = {}
    
    i = 0    
    for e1 in a1:
        if ((e1 in d) and (d[e1]!=a2[i])):
            print "XXX"
        d[e1] = a2[i]
        i += 1
        
    i = 0    
    for e1 in b1:
        if ((e1 in d) and (d[e1]!=b2[i])):
            print "XXX"
        d[e1] = b2[i]
        i += 1
        
    i = 0    
    for e1 in c1:
        if ((e1 in d) and (d[e1]!=c2[i])):
            print "XXX"
        d[e1] = c2[i]
        i += 1

    d['q'] = 'z'
    d['z'] = 'q'
        
    print d
    main(d)
    
    #l = []
    #for x in d.values():
        #l.append(x)
    #l.sort()
    #print l
    
    