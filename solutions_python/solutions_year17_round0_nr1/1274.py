import sys, getopt
import math

def flip(s,k):
    n_flips = 0
    i = 0
    print len(s),s
    l = len(s)
    if k==1:
        return s.count("-")
    while i <= l-k:
        print i,s,set(s[i:i+k]), n_flips, s[i:i+k]
        if len(set(s[i:i+k])) == 1 and list(set(s[i:i+k]))[0] == '-' and len(s[i:i+k])==k:
            print "bhua"
            n_flips = n_flips + 1
            s = s[0:i]+"".join(["+" for j in range(k)])+s[i+k:]
            i=i+k
            continue

        if s[i:i+k+1]=="-"+"".join(["+" for j in range(k-1)])+"-" and len(s[i:i+k+1])==k+1:
            print "yes" +"-"+"".join(["+" for j in range(k-1)])+"-"
            s = s[0:i]+ "".join(["+" for j in range(k+1)]) + s[i+k+1:]
            print "whoa" + s
            i = i+k+1
            n_flips = n_flips+2
            continue
        #if s[i]=="-" and len(s[i+1:].split("-")[0]) and len(s[i+1:].split("-")[0]) >= k:
        if s[i]=="-":
            print "here"
            new_s=s[0:i] + s[i:i+k].replace("+","p").replace("-","+").replace("p","-") + s[i+k:]
            print s,new_s
            s = new_s
            n_flips=n_flips+1
            i = i+1
            continue
        print "ok"
        i = i + 1
    if len(set(s))==1 and list(set(s))[0]=="+":
        res = str(n_flips)
    else:
        res =  "IMPOSSIBLE"
    print "res " + res
    return res

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
            s = line.split(" ")[0]
            k = int(line.split(" ")[1])
            res = flip(s,k)
            print "Case #%d: %d %s" % (count,k,res)
            f_out.write( "Case #%d: %s" % (count,res) +"\n")

        count = count + 1
    f_out.close()


if __name__ == "__main__":

   in_f = sys.argv[1]
   out_f = in_f.split(".")[-2]+".out"
   parseAndWrite(in_f,out_f)
   print in_f,out_f