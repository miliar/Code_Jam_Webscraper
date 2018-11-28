import re

def solve(chain,size):
    
    flip=0
    for index in range(len(chain)-size+1):
        if chain[index]=="-":
            flip+=1
            for flip_index in range(size):
                if chain[flip_index+index]=="-":
                    chain[flip_index+index]="+"
                else:
                    chain[flip_index+index]="-"
    
    all_happy=True
    for last_index in range(len(chain)-size,len(chain)):
        all_happy=all_happy and chain[last_index]=="+"
    
    if all_happy:
        return flip        
    else:
        return "IMPOSSIBLE"
            
if __name__ == "__main__":
    import fileinput
    input_f=open('/home/jaemin/workspace_liclipse/programming/input_output/A-large.in','r')
    output_f=open('/home/jaemin/workspace_liclipse/programming/input_output/A-large.out','w')
    T=int(input_f.readline())
    for case in range (1,T+1):
        chain,size=input_f.readline().rstrip("\n").split()
        
        answer=solve(list(chain),int(size))
        
        print("Case #%d: %s"%(case, answer))    
        output_f.write("Case #%d: %s\n"%(case, answer))
    input_f.close()
    output_f.close()
    
    