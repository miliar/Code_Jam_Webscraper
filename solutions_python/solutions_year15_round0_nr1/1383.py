#
def Ovation(caseno,counterlist,outfile):
    start_index = counterlist[0]
    line = mainlist[start_index].strip().split(" ")
    Smax = int(line[0])
    audiencelist = line[1]
    Djlist = 0
    sumjlist = 0
    sum1 = 0

    for i in range(1,Smax+1):
        if int(audiencelist[i]) == 0:
            sumjlist = sumjlist + int(audiencelist[i-1])
            Djlist = Djlist
            continue

        sum1 = sumjlist + int(audiencelist[i-1])

        sumjlist = sum1

        Djlist = max(abs(min(sum1 - i,0)),Djlist)

        sum1 = 0

    print >> outfile,  "Case #%d:"%(caseno + 1), Djlist



    counterlist[0] += 1


inputfile = open("large.in","r")
outfile = open("largeout.in",'w')
mainlist = inputfile.readlines()
inputfile.close()
T_maps = int(mainlist[0])
counterlist = [1]


for i in range(T_maps):
    Ovation(i,counterlist,outfile)


outfile.close()
