fr = open("in.txt","r")
fo = fr.readlines()
fw = open("out.txt","w")
for j in range(int(fo[0].strip('\n'))):
    n,m = [x for x in fo[j+1].strip('\n').split()]
    n = int(n)
    m = [int(x) for x in m]
    sum = m[0]
    c = 0
    for i in range(1,n+1):
#        print(i,sum,c)
        while(sum < i):
            c += 1
            sum += 1
        sum += m[i]
    s = "Case #"+str(j+1)+": "+str(c)+"\n"        
    fw.write(s)

fr.close()
fw.close()
    
            
