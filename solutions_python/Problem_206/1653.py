
import sys


def do(D,horses):
    t=0
    paths = []
    t_min = -1
    sorted_horses = sorted(horses,key=lambda x: x[0])
    for rev_i,h in enumerate(sorted_horses[::-1]):
        i = len(sorted_horses)-rev_i


        k = h[0]
        s = h[1]
        time_to_finish = (D-k)/float(s)

        print h
        if len(paths)==0:
            #t = t+time_to_finish
            paths = [(k,s,time_to_finish)]
            t_min = time_to_finish
        else:
            for path in paths:
                if time_to_finish < path[2]:
                    time_to_catch = abs((path[0]-k)/float(s-path[1]))
                    where_to_catch = s*time_to_catch+k


                    added_time = (where_to_catch-k)/float(s)

                    paths = [(k,s,time_to_catch)]+[(where_to_catch,path[1],(D-where_to_catch)/float(path[1]))]
                    t = t+added_time
                    break
                else:
                    t_min = time_to_finish


    max_speed = D/float(t_min)

    return max_speed

def parseAndWrite(in_f,out_f):
    f = open(in_f)
    f_out=open(out_f,"w")
    n_cases = None
    count = 1
    n_horses=0
    horses = []
    for line in f:
        print line
        if n_cases==None:
            n_cases=int(line)
            print "n cases: %d" % n_cases
        else:
            if n_horses==0:
                if len(horses) > 0:
                    print "Case #%d: %d %s" % (count,D,horses)
                    res = do(D,horses)
                    print "res: %f" % res
                    f_out.write( "Case #%d: %s" % (count,res) +"\n")
                    count = count + 1
                D = int(line.split(" ")[0])
                n_horses = int(line.split(" ")[1])
                horses = []
            else:
                k = int(line.split(" ")[0])
                s = int(line.split(" ")[1])
                horses.append((k,s))
                n_horses = n_horses-1



    print "Case #%d: %d %s" % (count,D,horses)
    res = do(D,horses)
    print "res: %f" % res
    f_out.write( "Case #%d: %s" % (count,res) +"\n")
    f_out.close()


if __name__ == "__main__":

   in_f = sys.argv[1]
   out_f = in_f.split(".")[-2]+".out"
   parseAndWrite(in_f,out_f)
   print in_f,out_f