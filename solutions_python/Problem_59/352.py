
import sys
from sets import Set

if __name__ == '__main__':

    if len(sys.argv)> 1:
        file_name = sys.argv[1]
    else:
        file_name  = "A-large.in"

    filei = open(file_name)
    fileo = open(file_name + ".out", "w+")
    i = 1
    line = filei.readline()
    num_inputs = int(line)
    
    while True:

        exists = Set()
        
        count = 0
        line = filei.readline()
        nk = line.split(" ")

        
        N = int(nk[0])
        K = int(nk[1])
        
        n = 0
        while n < N:
            line = filei.readline()
            path = line.split("/")
            p = line.strip().split("/")
            t = ""
            for s in p:
                if len(s.strip()) > 0:
                    t += "/" +s
                #print "t=", t
                if len(s.strip()) > 0 and (not t in exists):
                    exists.add(t)
            exists.add(line)
            n += 1
            
        k = 0
        while k < K:
            line = filei.readline()
            #print "line", line
            p = line.strip().split("/")
            t = ""
            for s in p:
                if len(s.strip()) > 0:
                    t += "/" +s
                print "t=", t
                if len(s.strip()) > 0 and (not t in exists):
                    
                    count += 1
                    #print "adding ", t, count
                    exists.add(t)
            k += 1
        print >> fileo, "Case #%d: %s" % (i, count)

        
        if i == num_inputs:
            break
        i += 1
    fileo.flush()
    filei.close
    fileo.close
        

    
