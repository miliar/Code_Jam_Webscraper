#f = open('D-small-attempt0.in', 'r')
#f = open('D-sample.in', 'r')
f = open('D-large.in', 'r')
outpu=open('output.txt','w')
cases = int(f.readline())
for case in range(cases):
    f.readline()
    N = [float(x)  for x in f.readline().split(" ")]
    K = [float(x)  for x in f.readline().split(" ")]
    N.sort(),K.sort()
    NCW =0
    # playing war
    ni,ki = -1,-1
    while ki< len(K):
        ni,ki=ni+1,ki+1
        while (ki<len(K)) and (N[ni]>K[ki]):
            ki=ki+1
    NCW= len(N) - ni
    #playing deceitful war
    ni,ki = -1,-1
    while ni< len(N):
        ni,ki=ni+1,ki+1
        while (ni<len(N)) and (K[ki]>N[ni]):
            ni=ni+1
    NCDW=ki
    outpu.write('Case #'+ str(case+1)+": "+str(NCDW)+ " "+str(NCW)+"\n")#"Impossible"
f.close()
outpu.close()
