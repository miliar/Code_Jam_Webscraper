import sys


if __name__ == "__main__":
    f = open( "small.in" )
    g = open( "output_small.txt","w" )
    #g = sys.stdout

    numcases = f.readline()

    caseI = 1
    line = f.readline()
    while line != "":
        nums = [ int(x) for x in line.split() ]
        nums = nums[1:]

        nums.sort()

        s = {}
        s[0] = [0]

        s1 = []
        s2 = []
        for x in nums:
            k = list(s.keys())
            for y in k:
                z = s.get(x+y,0)
                if z == 0:
                    s[x+y] = list(s[y])
                    s[x+y].append( x )
                else:
                    s1 = z
                    s2 = list(s[y])
                    s2.append(x)
                    break
            if len(s1) > 0 and len(s2) > 0:
                break
        if len(s1) == 0 or len(s2) == 0:
            output = "Impossible"
        else:
            s1.remove(0)
            s2.remove(0)
            #print sum(s1),sum(s2)
            output = " ".join( ["%s"%x for x in s1] ) + "\n" + " ".join( ["%s"%x for x in s2] )
        
        g.write( "Case #%s:\n%s\n"%(caseI,output) )
        caseI += 1
        line = f.readline()
    f.close()
    g.close()
