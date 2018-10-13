f=open("input.in","r")
o=open("output.txt","w")

T=int(f.readline().strip())

for i in range(1,T+1):
    o.write("Case #{}: ".format(i))
    line=int(f.readline().strip())
    num1=line
    
    for j in range(line):
        num=list(str(num1))
        num_s=list(str(num1))
        num_s.sort()
        #print(num)
        #print(num_s)
        if num==num_s:
            o.write("".join(num)+"\n")
            break
        else:
            num1-=1

f.close()
o.close()
    
print("Done")
