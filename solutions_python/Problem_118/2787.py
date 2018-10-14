import math
f=open(r'd:\C-small-attempt.in','r')
fout=open(r'd:\sol_fair.out','w')
t=int(f.readline())
for i in range(0,t):
    count=0
    a,b=map(int,f.readline().split())
    sqa = math.sqrt(a)
    sqb = math.sqrt(b)
    if sqa==int(sqa):
        sqa=int(sqa)
    else:
        sqa=int(sqa)+1
    sqb=int(sqb)
    for j in range(sqa,sqb+1):
        sa=str(j)
        ssa=str(j**2)
        if sa==sa[::-1] and ssa==ssa[::-1]:
            count+=1
    fout.write("Case #")
    fout.write(str(i+1))
    fout.write(":")
    fout.write(" ")
    fout.write(str(count))
    fout.write("\n")
f.close()
fout.close()
    
        
        
    
