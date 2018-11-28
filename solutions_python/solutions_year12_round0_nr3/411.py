
in_file = open("C-small.in","r");
out_file = open("C.out","w");
casenum = 0;

for line in in_file:
    if (casenum == 0):
        casenum += 1
        continue
    tmp = line.split()
    A = int(tmp[0])
    B = int(tmp[1])
    
    ans = 0
    for i in xrange(A,B):
        #print str(casenum) + ":" + str(i)
        str_i = str(i)
        j = str_i[-1] + str_i[:-1]
        while str_i != j:
            #print j
            int_j = int(j)
            if (i < int_j and int_j <= B):
                if (casenum == 2):
                    print str(casenum) + ": "+str(i)+"/"+j
                ans += 1
            j = j[-1] + j[:-1]
    
    print ans
    out_file.write("Case #"+str(casenum)+": "+str(ans)+"\n")
    casenum += 1;

out_file.close()
