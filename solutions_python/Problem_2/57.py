#!/usr/bin/python

import mpmath
import copy
import sys
#import pp

def resolve(from_a_d,from_a_a,from_b_d,from_b_a):
    a = 0
    b = 0

    llegan_a = []
    llegan_b = []
    while (from_a_d.__len__() + from_b_d.__len__() > 0):

        min_a_d = 1440
        min_a_a = 1440
        min_b_d = 1440
        min_b_a = 1440

        if from_a_d.__len__() > 0:
            min_a_d = min(from_a_d)

        if from_a_a.__len__() > 0:
            min_a_a = min(from_a_a)

        if from_b_d.__len__() > 0:
            min_b_d = min(from_b_d)

        if from_b_a.__len__() > 0:
            min_b_a = min(from_b_a)


        if min_a_d < min_b_d:

            if min_a_d < min_b_a:
                a+=1
            else:
                from_b_a.remove(min_b_a)    
            from_a_d.remove(min_a_d)
        else:
            if min_b_d < min_a_a:
                b+=1
            else:
                from_a_a.remove(min_a_a)    
            from_b_d.remove(min_b_d)


    return "%d %d" % (a,b)

def read_in():
    fd = open("in")

    n = int(fd.readline())
    out=[]
    #parallel = pp.Server(ppservers=(),secret="")
    #threads = []
    for i in xrange(n):
        print "Create: %d       \r"%(i),
        sys.stdout.flush()



        T = int(fd.readline())
        line = fd.readline().split(" ")

        NA = int(line[0])
        NB = int(line[1])

        from_a_d = []
        from_a_a = []
        for j in xrange(NA):
            line =fd.readline().split(" ")
            from_a_d.append(int(line[0].split(":")[1])+60*int(line[0].split(":")[0]))
            from_a_a.append(int(line[1].split(":")[1])+60*int(line[1].split(":")[0])+T)

        from_b_d = []
        from_b_a = []
        for j in xrange(NB):
            line =fd.readline().split(" ")
            from_b_d.append(int(line[0].split(":")[1])+60*int(line[0].split(":")[0]))
            from_b_a.append(int(line[1].split(":")[1])+60*int(line[1].split(":")[0])+T)
        


        ######
        #func = resolve
        #args = (None,)
        #depfuncs = (None,)
        #depmodules = (None,)
        ######

        #threads.append(parallel.submit(func,args,depfuncs,depmodules))



    #for i in xrange(threads.__len__()):
    #    print "Join: %d           \r"%(i+1),
    #    sys.stdout.flush()
    #    out.append("Case #%d: %s"%(i+1,threads[i]()))
        out.append("Case #%d: %s"%(i+1,resolve(from_a_d,from_a_a,from_b_d,from_b_a)))

    return "\n".join(out)



print read_in()

