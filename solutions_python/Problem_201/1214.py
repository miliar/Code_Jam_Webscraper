import heapq

MAXINDEX=10**18

def solve(N,K):
    h=[]
    heapq.heappush(h,(MAXINDEX-(N+1)//2,MAXINDEX-(N+1 -(N+1)//2),MAXINDEX-(N+1)//2))
    
    for i in range(K):
        info=heapq.heappop(h)
        d1=MAXINDEX-info[0]
        d2=MAXINDEX-info[1]
        pos=MAXINDEX-info[2]
        s=pos-d1
        e=d2+pos
        left_middle=(s+pos)//2
        right_middle=(e+pos)//2
        heapq.heappush(h,(MAXINDEX-(left_middle-s),MAXINDEX-(pos-left_middle),MAXINDEX-left_middle))
        heapq.heappush(h,(MAXINDEX-(right_middle-pos),MAXINDEX-(e-right_middle),MAXINDEX-right_middle))
            
            
    return d2-1,d1-1      
            
if __name__ == "__main__":
    import fileinput
    input_f=open('/home/jaemin/workspace_liclipse/programming/input_output/C-small-2-attempt0.in','r')
    output_f=open('/home/jaemin/workspace_liclipse/programming/input_output/C-small-2-attempt0.out','w')
    T=int(input_f.readline())
    for case in range (1,T+1):
        [N,K]=[int(x) for x in input_f.readline().split()]
        
        a1,a2=solve(N,K)
        
        print("Case #%d: %s %s"%(case, a1,a2))    
        output_f.write("Case #%d: %s %s\n"%(case, a1,a2))
    input_f.close()
    output_f.close()
    
    