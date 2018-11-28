with open("in.txt", "r") as in_file:
    cases = int( in_file.readline() )
    for case in range(1,cases+1):
        smax, shyppl = in_file.readline().split(" ")
        smax = int(smax)
        curppl = []
        
        print "Case #" + str(case) + ":",
        totalppl = 0
        neededppl = 0
        for ppl in range(smax+1):
            #print ppl, shyppl[ppl]
            
            neededppl += max(0, ppl-totalppl)
            totalppl += int(shyppl[ppl]) + max(0, ppl-totalppl)
 
        print neededppl

