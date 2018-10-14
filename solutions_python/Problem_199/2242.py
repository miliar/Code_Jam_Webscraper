
fin = open('A-large.in','r')
fout = open('opl.in','w')
T = int(fin.readline())
for i in range(0,T):
    s,k =fin.readline().split()
    count = 0
    s=list(s)
    k=int(k)
    c = '-'
    check=0
    out = out = "case #" + str(i+1) + ": " 
    while(1):
        if c in s :
            x = s.index(c)
            #print(x)
            if x<=len(s)-k:
                count = count+1
                for j in range(0,k):
                    if s[x] =="+" :
                        s[x] = "-"
                    else :      
                        s[x]="+"
                    x = x+1
                #print(s)
            else:
                out = out+"IMPOSSIBLE"+"\n"
                fout.write(out)
                check=1
                break
                
        else:
            break
    if check == 0 :
        out = out +  str(count) + "\n"
        fout.write(out)

fin.close()
fout.close()

