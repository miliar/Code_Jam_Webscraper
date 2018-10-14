

def get_cycle(n, B):
    
    s = str(n)
    l = []
    sum = 0
    for es in s[:]:
        s = s[1:] + s[0]
        if ((int(s) > n) and (int(s) <= B)):
            if (int(s) not in l):
                #print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                
                l.append(int(s))
                sum += 1
    return sum,l



def main():
    inpfile = open("C-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()

        a = int(linelst[0])
        b = int(linelst[1])
        
        #print a,
        #print b
        S = 0
        
        for e in range(a,b):
            x,l = get_cycle(e, b)
            #print str(e) + ": " + str(l)
            S += x

        
        result = "Case #" + str(case) + ": " + str(S)+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":

    #print get_cycle(12345, 55222)
    
    main()
    

    
    