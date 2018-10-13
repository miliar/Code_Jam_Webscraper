
with open("D:/Studies/Online Competitions/Google codejam/A-large.in" ,"r") as f:
    lines = f.readlines()

f.close()    

n = int(lines[0])
#print(n)
with open("D:/Studies/Online Competitions/Google codejam/A-large-output.txt" ,"w") as f:
    for outer in range(1,n+1):
        s , k = lines[outer].split(' ')
        p = []
        x = len(s)
        for i in range(x):
            p.append(s[i])
        k = int(k)
        ans = 0
        for i in range(x-k+1):
            if p[i] == '-':
                ans +=1
                for j in range(i,i+k):
                    if p[j] == '-':
                        p[j] = '+'
                    else:
                        p[j] = '-'

            
                
        a = 0
        #print(p,len(p))
        for i in range(x):
            if p[i] == '-':
                a = 1
                break
        
        if(a==0):
            print("Case #",outer,": ",ans)
            x = "Case #"+str(outer)+": "+str(ans)
            f.write(x)
            f.write("\n")
        else:
            print("Case #",outer,": IMPOSSIBLE")
            x = "Case #"+str(outer)+": IMPOSSIBLE"
            f.write(x)
            f.write("\n")
        
f.close()
   
