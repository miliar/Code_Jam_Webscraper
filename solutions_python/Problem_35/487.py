import os


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def watershed(path=os.path.expanduser("~")+"/"+"/Desktop/jam/"):
    fin=open(path+"B-small-attempt0.in", "r")
    fout = open(path+"out2.txt", "w")

    test_cases_count = fin.readline()
    print "No of test cases == %s" % test_cases_count

    for i in range(int(test_cases_count)):
        sinks = {}
        sink_loc = {}
        sink_val = {}
        sink_trace = {}

        dimension = fin.readline().strip().split(" ")
        for j in range(int(dimension[0])):
            sinks[j] = fin.readline().strip().split(" ")
#        print "SINK %s is: %s" % (i+1, sinks)
        

        k = int(dimension[1])
        j = int(dimension[0])

        klist = range(k)
        jlist = range(j)
 
        klist.reverse()
        jlist.reverse()
 
        k = k-1
        j = j-1 

        for n in jlist:
            sink_loc[n] = []
            sink_val[n] = []
            sink_trace[n] = []
            for m in klist:
                sink_loc[n].append(0)
                sink_val[n].append(0)
                sink_trace[n].append(0)

        for m in klist:
            for n in jlist:
                val = sinks[n][m]

                if n > 0:
                    temp = sinks[n-1][m]
                    if temp < val:
                        sink_loc[n][m]=[n-1, m]
                        val = temp

                

                if m > 0:
                    temp = sinks[n][m-1]
                    if temp < val:
                        sink_loc[n][m]=[n, m-1]
                        val = temp

                if m < k:
                    temp = sinks[n][m+1]
                    if temp < val:
                        sink_loc[n][m]=[n, m+1]
                        val = temp
                        
                if n < j:
                    temp = sinks[n+1][m]
                    if temp < val:
                        sink_loc[n][m]=[n+1, m]
                        val = temp
                
        
 #        print sink_loc
        distinct_list = {}
        list_count = 0
        
        sink_trace_list = []
        link_key = ''
        
        fout.write("Case #"+str(i+1)+ ":\n")
        for n in jlist:
            for m in klist:
                sink_trace[n][m] = trace(sink_loc, n, m)

        klist.reverse()
        jlist.reverse()

        for n in jlist:
            for m in klist:
                temp = sink_trace[n][m]
                
                if temp in sink_trace_list:
                    for i in distinct_list:
                        if distinct_list[i] == temp:
                            link_key = i
                            break
                else:
                    distinct_list[alpha[list_count]] = temp
                    link_key = alpha[list_count]
                    list_count += 1
                    sink_trace_list.append(temp)
                    
                fout.write(link_key+ " ")
                
            fout.write("\n")

#        print "\nALL SINKS: %s" % sink_trace
#        print "\nALPHA VALUES:%s \n " % distinct_list
    fout.close()
    fin.close()

def trace(sink_nloc, i, j):
    
    temp = sink_nloc[i][j]
    if temp == 0:
        return [i, j]
    else:
        return trace(sink_nloc, temp[0], temp[1])

watershed()
