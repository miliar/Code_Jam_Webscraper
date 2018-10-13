
with open("D:/Studies/Online Competitions/Google codejam/B-large.in" ,"r") as f:
    lines = f.readlines()

f.close()    

n = int(lines[0])
#print(n)
with open("D:/Studies/Online Competitions/Google codejam/B-large-output.txt" ,"w") as f:
    for outer in range(1,n+1):
        p = lines[outer].strip('\n')
        x = len(p)
        a = []
        for i in range(x):
            a.append(int(p[i]))
        a.append(0)
        
        for y in range(20):
            for i in range(x-1):
                if a[i+1] < a[i]:
                    a[i] -= 1
                    for j in range(i+1,x+1):
                        a[j] = 9
                    break    

        print(a)
        s = 0
        if a[0] != 0:
            s =  a[0]
        for i in range(1,len(a)-1):
            s = s*10 + a[i]
        x = "Case #"+str(outer)+": "+str(s)
        f.write(x)
        f.write("\n")
        
f.close()
   
