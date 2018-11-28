def outp(a,b):
    file=open("output.txt","a")
    s="Case #"+str(a+1)+": "+str(b)+"\n"
    file.write(s)
    file.close
    print(s)

q=open ("output.txt","w")
q.close()
inp = open("B-large.in","r")
a= []
for line in inp:
    if "\n" in line:
        a.append(line[0:-1])
    else:
        a.append(line)
inp.close()
inpNum =int(a.pop(0))
for ii in range(inpNum):
    N = list(a[ii])
    N = [int(x) for x in N]
    tidy=[]
    broke = False
    for i in range(len(N)):
        if broke == True:
            tidy.append(9)
        elif i==0 or N[i] >= N[i-1]:
            tidy.append(N[i])
        else:
            broke = True
            tidy[i-1] -= 1
            for p in range(i-2, -1, -1):
                if tidy[p]<=tidy[p+1]:
                    break
                tidy[p+1] = 9
                tidy[p] -= 1
            tidy.append(9)
    tidy = "".join(map(str, tidy))
    tidy = tidy.strip('0')
    outp(ii, tidy)
            
    
            
    
    
    
