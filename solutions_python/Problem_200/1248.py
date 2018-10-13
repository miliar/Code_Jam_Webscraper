import re

def solve(N):
    result=[]
    for i in range(len(N)):
        result.append(int(N[i]))
    
    for i in range(len(N)-1,-1,-1):
        if i-1 >=0:
            if result[i-1]>result[i]:
                result[i-1]-=1
                for trailing_index in range(i,len(N)):
                    result[trailing_index]=9
            
    return int("".join(map(str,result)))        
            
if __name__ == "__main__":
    import fileinput
    input_f=open('/home/jaemin/workspace_liclipse/programming/input_output/B-large.in','r')
    output_f=open('/home/jaemin/workspace_liclipse/programming/input_output/B-large.out','w')
    T=int(input_f.readline())
    for case in range (1,T+1):
        N=input_f.readline().rstrip("\n")
        
        answer=solve(N)
        
        print("Case #%d: %s"%(case, answer))    
        output_f.write("Case #%d: %s\n"%(case, answer))
    input_f.close()
    output_f.close()
    
    