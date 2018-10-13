import math

def is_palindrome(nb):
    tmp=str(nb)
    if len(tmp)==1:
        return True
    
    i=0
    j=len(tmp)-1
    while i<j:
        if tmp[i]!=tmp[j]:
            return False
        i+=1
        j-=1
    return True   
    
def solve(A,B):
    cnt=0
    for i in range(A,B+1):
        if is_palindrome(i):            
            tmp=math.sqrt(i)
            if tmp.is_integer():
                if is_palindrome(int(tmp)):
                    cnt+=1
    return cnt
        
#Main
f=open("C-small-attempt0.in","r")
lines=f.readlines()
f.close()

N_cases=eval(lines[0])
solutions=[]

for i in range(1,N_cases+1):
    tmp=lines[i].split()
    A=eval(tmp[0])
    B=eval(tmp[1])

    solution="Case #"+str(i)+": "+str(solve(A,B))+"\n"
    solutions.append(solution)
    print("Case #"+str(i)+" done.")


f=open("o.in","w")
f.writelines(solutions)
f.close()
    
