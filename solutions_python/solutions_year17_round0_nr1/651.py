fin="alargein.txt"
fout="alargeout.txt"
file = open(fin, "r")
t=int(file.readline())

a=[]
ans=[]
for i in range(t):
    a.append(file.readline().split(' '))
    a[i][1] = int(a[i][1])
    a[i][0] = list(a[i][0])


    j=0
    f=0
    while j<len(a[i][0])-a[i][1]+1:
        if a[i][0][j] == '+':
            j=j+1
            continue
        else:
            for k in range(a[i][1]):
                if a[i][0][j+k] == '+':
                    a[i][0][j+k] = '-'
                else:
                    a[i][0][j+k] = '+'

            f=f+1

    while j<len(a[i][0]):
        if a[i][0][j] == '-':
            ans.append("IMPOSSIBLE")
            break
        j=j+1
        

    if j== len(a[i][0]):
        ans.append(str(f))


file.close()
file = open(fout, "w")

for i in range(t):
    file.write("Case #"+str(i+1)+": "+ans[i]+'\n')
file.close()
