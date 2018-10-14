#!/usr/bin/env python

with open("A-small-attempt1.in", "r") as fin:
    N = int(fin.readline())
    fout = open("A-small-attempt1.out", "w")

    # read the input
    for i in xrange(N):
        num = int(fin.readline())
        ss = []
        possible = True
        for p in xrange(num):
            ss.append(fin.readline().replace("\n", ""))
        consec = []
        for p in xrange(num):
            ch = []
            freq = []
            tn = 0
            for q in xrange(len(ss[p])):
                if tn == 0:
                    tn +=1
                    ch.append(ss[p][q])
                    while q+1!=len(ss[p]) and ss[p][q] == ss[p][q+1]:
                        tn += 1
                        q += 1
                    
                    freq.append(tn)
                    tn -= 1
                else:
                    tn -= 1
            consec.append((ch, freq))
        tmp = consec[0][0]
        for p in xrange(1, num):
            if consec[p][0] != tmp:
                possible = False
        print possible
        if not possible:
            fout.write("Case #"+ str(i+1)+ ": Fegla Won\n")
        else:
            sum = 0
            for p in xrange(len(tmp)):
                s = 0.0
                for q in xrange(num):
                    s += consec[q][1][p]
                s = round(s/num)
                for q in xrange(num):
                    sum += abs(consec[q][1][p]-s)
                sum = int(sum)
            fout.write("Case #"+str(i+1)+": "+str(sum)+"\n")

                        
                        