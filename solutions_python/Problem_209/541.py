rnd="p17R1C"
pb="A"
size="large(2)"
fin=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.in"%(rnd,pb,size),'r')
fout=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.out"%(rnd,pb,size),'w')

import math
T=int(fin.readline())
#print T
for i in range(1,T+1):
    sN,sK=fin.readline().strip().split()
    N,K=int(sN),int(sK)
    
    RHs=[[int(e) for e in fin.readline().strip().split()] for j in range(N)]
    cand=[]
    for largest_served_R in list(set(sorted([e[0] for e in RHs])[-(N-K+1):])):
        #print largest_served_R,
        #unstack thickest largerst:
        bottom=[largest_served_R, max([e[1] for e in RHs if e[0]==largest_served_R])]
        unRHs=RHs[:]
        unRHs.remove(bottom)
        #print "***",unRHs
    
        served_side_surfs=sorted([(e[1]*e[0]*2.0*math.pi) for e in unRHs if e[0]<=largest_served_R])[-K+1:] if K>1 else []
        #print served_side_surfs,"/",(sum(served_side_surfs), math.pi*largest_served_R**2),sum(served_side_surfs) + math.pi*largest_served_R**2,
        
        cand.append(float(bottom[0]*bottom[1])*2.0*math.pi+sum(served_side_surfs) + math.pi*largest_served_R**2)
        #print cand
    res=max(cand)
        
        

            
    line="Case #%d: %.6f" % (i, res)
    print line
    fout.write(line+"\n")
fout.close()