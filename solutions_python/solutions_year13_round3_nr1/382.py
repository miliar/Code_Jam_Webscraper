import sys

fout = open("answers.out", "w")
fin = open("A-small-attempt0.in", "r")

T=int(fin.readline())
results=[]
for t in range(T):
    s=fin.readline().split()
    name=s[0]
    n=int(s[1])
    length=len(name)
    result=0
    for i in range(n,length+1):
        for j in range(0,length-i+1):
            m=0
            for k in range(j,j+i):
                if(not(name[k] in ['a','e','i','o','u'])):
                    m+=1
                else:
                    m=0
                if(m==n):
                    result+=1
                    break
    results.append(result)


for t in range(T):
    fout.write("Case #")
    fout.write(str(t+1))
    fout.write(": ")
    fout.write(str(results[t]))
    fout.write("\n")
fout.close()

