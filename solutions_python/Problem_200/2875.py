
fin = open('2.in')
fout = open('2.out', 'w')


n = int(fin.readline())

for t in range(0, n):
    str = fin.readline()
    num = []
    l = len(str) - 1
    if str[l]>='0' and str[l]<='9':
        l = l+1
    for i in range(0,l):
        num.append(int(str[i]))
    for i in range(1,l):
        if num[i-1]>num[i]:
            num[i-1] = num[i-1]-1
            for j in range(i,l):
                num[j] = 9
            break
    

    for j in range(1,i):
        k = i-j
        if num[k]<num[k-1]:

            num[k] = 9
            num[k-1] = num[k-1]-1
        
        
    fout.write("Case #%d: " %(t+1))
    for i in range(0, l):
        if num[i] > 0:
            fout.write("%d" %(num[i]))
            
    fout.write("\n")
    
    del(num[:])

fin.close();
fout.close();