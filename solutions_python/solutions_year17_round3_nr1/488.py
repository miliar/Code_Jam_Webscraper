import numpy as np


def solve(N,K,RH):
    max_surface=0
    
    RH.sort(key=lambda x:x[0],reverse=True)
    
    for i in range(N-K+1):
        r,h=RH[i]
        tails=sorted(RH[i+1:],key=lambda x:x[0]*x[1],reverse=True)
        side_area=2*r*h+sum([2*x*h for x,h in tails[:K-1]])
        max_surface=max(max_surface,r**2+side_area)
            
    return np.pi*max_surface        
            
if __name__ == "__main__":
    import fileinput
    input_f=open('/home/jaemin/workspace_liclipse/programming/input_output/A-large.in','r')
    output_f=open('/home/jaemin/workspace_liclipse/programming/input_output/A-large.out','w')
    T=int(input_f.readline())
    for case in range (1,T+1):
        [N,K]=[int(x) for x in input_f.readline().split()]
        
        RH=[]
        for _ in range(N):
            RH.append([int(x) for x in input_f.readline().split()])
        
        answer=solve(N,K,RH)
        
        print("Case #%d: %s"%(case, answer))    
        output_f.write("Case #%d: %s\n"%(case, answer))
    input_f.close()
    output_f.close()
    
    