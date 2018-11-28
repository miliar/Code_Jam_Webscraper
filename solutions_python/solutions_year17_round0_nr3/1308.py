import math
import sys, getopt

def getThatNumber(n,k):
    print n,k
    ls = int(math.floor((n-1) /float(2)))
    rs = int(math.ceil((n-1) /float(2)))
    stalls = set([n])
    counts = {}
    counts[n] = 1
    #print n,ls,rs
    i=0
    while i<k:
        depth = int(math.floor(math.log(i+1,2)))
        #print depth
        chosenStall = max(stalls)

        how_many_left = counts[chosenStall]
        how_many_to_split = min(how_many_left,k-i)
        counts[chosenStall] = counts[chosenStall]-how_many_to_split
        if counts[chosenStall]==0:
            stalls.remove(chosenStall)
            del counts[chosenStall]


        ls = int(math.floor((chosenStall-1) /float(2)))
        rs = int(math.ceil((chosenStall-1) /float(2)))
        stalls.add(ls)
        stalls.add(rs)
        counts[ls] = counts.get(ls,0)+how_many_to_split
        counts[rs] = counts.get(rs,0)+how_many_to_split

        i = i + how_many_to_split
        #print sorted(list(stalls) ),chosenStall,ls,rs
    return max([ls,rs]),min([ls,rs])

def parseAndWrite(in_f,out_f):
    f = open(in_f)
    f_out=open(out_f,"w")
    n_cases = None
    count = 0
    for line in f:
        print line
        if n_cases==None:
            n_cases=int(line)
            print "n cases: %d" % n_cases
        else:
            n = int(line.split(" ")[0])
            k = int(line.split(" ")[1])
            y, z = getThatNumber(n,k)
            print "Case #%d: %d %d" % (count,y,z)
            f_out.write( "Case #%d: %d %d" % (count,y,z) +"\n")

        count = count + 1
    f_out.close()


if __name__ == "__main__":

   in_f = sys.argv[1]
   out_f = in_f.split(".")[-2]+".out"
   parseAndWrite(in_f,out_f)
   print in_f,out_f