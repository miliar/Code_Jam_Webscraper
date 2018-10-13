import sys, getopt

def indexAtWhichDecreases(n):
    n_str = str(n)
    previousNumber = None
    for ind,val in enumerate(n_str):
        if previousNumber is None:
            previousNumber=int(val)
        else:
            if int(val)<previousNumber:
                return ind
        previousNumber=int(val)
    return 0


def getThatNumber(n):
    my_n = n
    while indexAtWhichDecreases(my_n)>0:
        i = indexAtWhichDecreases(my_n)
        r = int(str(n)[i:])
        my_n = n-r-1
    return my_n

def parseAndWrite(in_f,out_f):
    f = open(in_f)
    f_out=open(out_f,"w")
    n_cases = None
    count = 0
    for line in f:
        print int(line)
        if n_cases==None:
            n_cases=int(line)
        else:
            print "Case #%d: %d" % (count,getThatNumber(int(line)))
            f_out.write( "Case #%d: %d" % (count,getThatNumber(int(line))) +"\n")

        count = count + 1
    f_out.close()



if __name__ == "__main__":

   in_f = sys.argv[1]
   out_f = in_f.split(".")[-2]+".out"
   parseAndWrite(in_f,out_f)
   print in_f,out_f
