import math                  # math module in python

def D(alist):
    alist.sort()
    if len(alist) == 1 and alist[0] == 0:
        return 0
    else:
        if len(alist) > 1 and alist[-1] - alist[0] == 0 and alist[0] == 1:
            if alist[-1] != 1:
                print "yes"
            return alist[-1]

        else:
            if len(alist) == 1 and alist[0] == 1:
                return alist[0]
            else:
                if alist[-1] == 4 or alist[-1] == 9:
                    N = int(math.sqrt(alist[-1]))
                else:
                    N = int(alist[-1] / 2)

                # use all the sums of the number

                holder = alist[-1]

                blist = alist[:]

                for i in range(len(blist)):
                    blist[i] -= 1
                while 0 in blist:
                    index = blist.index(0)
                    blist.pop(index)

                alist[-1] = holder - N
                alist.append(N)

            

            return min( 1 + D(blist), D(alist) + 1)

def Solve(caseno,counterlist,outfile):
    start_index = counterlist[0]
    number_diners = int(mainlist[start_index])
    alist = [int(item) for item in mainlist[start_index + 1].strip().split(" ")]
    ans = D(alist)

    print>> outfile, "Case #%d:"%(caseno + 1), ans

    counterlist[0] = start_index + 2
    



inputfile = open("small.in","r")
outfile = open("smallout2.in",'w')
mainlist = inputfile.readlines()
inputfile.close()
T_maps = int(mainlist[0])
counterlist = [1]



for i in range(T_maps):
    Solve(i,counterlist,outfile)
##    raw_input("Enter")



outfile.close()



