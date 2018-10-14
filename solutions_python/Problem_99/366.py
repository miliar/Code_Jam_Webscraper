
from itertools import * 





                

def main():
    inpfile = open("A-small-attempt0.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        line2 = inpfile.readline().strip()
        linelst = line.split()
        linelst2 = line2.split()
        
        A = int(linelst[0])
        B = int(linelst[1])

        #print line
        #print linelst2
        
        ll = []
        
        for x in linelst2:
            ll.append([float(x), 1-float(x)])

        #print ll
        #print "------------"
        
        
        pcase1 = 1.0
            
        for x in linelst2:
            ix = float(x)
            pcase1 *= ix
        #print pcase1
            
        expect1 = (B - A + 1) * pcase1 + (2*B - A + 2) * (1 - pcase1)
        #print expect1
        
        Min = expect1
        for i in range(1, A + 1):
            p = 1.0
            for x in linelst2[:-i]:
                ix = float(x)
                p *= ix
            #print p
            expect = p * (B - A + 1 + 2*i) + (2*B - A + 2 + 2*i) * (1 - p)
            #print expect
            if expect < Min:
                Min = expect
                
        f = B + 2
        if f < Min:
                Min = f
                
        #print Min
            
        r = int(Min*1000000)
        r = str(r)
        #print r
        r1 = r[:-6]
        r2 = r[-6:]
        #print r1, r2

        result = "Case #" + str(case) + ": " + str(r1)+"."+r2+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":
    main()
    
    
    