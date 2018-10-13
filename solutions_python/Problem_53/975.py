import re
filename = 'A-small-attempt2'
infilename = filename+'.in'
outfilename = filename+'.out'
infile = open(infilename,'r')
outfile = open(outfilename,'w')
print infile
ntestcases = infile.readline(5)
print infile.readline()
print "Solving", ntestcases, "test cases."
i=0
results=[]

def solve(i,n,k):
    #print "Solving test case #" + str(i)+" with", n, "snappers and", k, "snaps."
    iteration = 0
    state=[]
    while iteration<n:
        if iteration != 0:
            state.append(['unpowered','off'])
        else:
            state.append(['powered','off'])
        iteration=iteration+1

    iteration = 0
    while iteration<k:
        #print "   Snap #"+str(iteration+1)
        for snappernum in range(0,len(state)):
            if state[snappernum][0]=='powered':
                if state[snappernum][1]=='off':
                    state[snappernum][1]='on'
                else:
                    state[snappernum][1]='off'
            if snappernum != 0:
                if state[snappernum-1][0]=='powered' and state[snappernum-1][1]=='on':
                    state[snappernum][0]='powered'
                else:
                    state[snappernum][0]='unpowered'
        #print "   Result of snap #"+str(iteration+1)+":", state
        #if state[len(state)-1][0]=='powered' and state[len(state)-1][1]=='on':
            #print "   Because the last snapper (snapper #"+str(len(state))+") is powered and on, the light is ON."
        #elif state[len(state)-1][0]=='unpowered' and state[len(state)-1][1]=='on':
            #print "   Because the last snapper (snapper #"+str(len(state))+") is on but unpowered, the light is OFF."
        #elif state[len(state)-1][0]=='powered' and state[len(state)-1][1]=='off':
            #print "   Because the last snapper (snapper #"+str(len(state))+") is powered but off, the light is OFF."
        #else:
            #print "   Because the last snapper (snapper #"+str(len(state))+") is unpowered and off, the light is OFF."
        iteration=iteration+1
    if state[len(state)-1][0]=='powered' and state[len(state)-1][1]=='on':
        return 'ON'
    else:
        return 'OFF'
    #for snapnum in range(0,len(results)):
        #print "      After snap #" + str(snapnum+1) + ", the light was", results[snapnum]
        
while i<int(ntestcases):
    line=infile.readline()
    line = line.rstrip()
    parsedline = re.split(":? ", line, 2)
    results.append(solve(i+1, int(parsedline[0]),int(parsedline[1])))
    i=i+1
    
formattedresults = ""
for casenum in range(0,int(ntestcases)):
    formattedresults = formattedresults + "Case #" + str(casenum+1) + ": " + results[casenum] + "\n"

print "\n  Results:"
print formattedresults
print "Writing results to", outfilename
print outfile
outfile.write(formattedresults)
print "Done."
outfile.close()
