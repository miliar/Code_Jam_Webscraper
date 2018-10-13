fin="B-large.in"
fout="blargeout.txt"
file = open(fin, "r")
t=int(file.readline())

a=[]
ans=[]
for i in range(t):
    inp = map(int, list(file.readline().strip()))
    a.append(inp)
    print a

for i in range(t):
    result = ""
    
    j=0
    while j < len(a[i])-1:
        print j, result
        if a[i][j]>a[i][j+1]:
            result = result + str(a[i][j] - 1)
            break
        elif a[i][j] == a[i][j+1]:
            k = j
            temp = '' 
            while k < len(a[i]) and a[i][k] == a[i][j]:
                temp = temp + str(a[i][k]) 
                k=k+1
            if k < len(a[i]) and a[i][k] < a[i][j]:
                result = result + str(a[i][j] - 1)
                break
            result = result + temp
            j = k
            
            
        else:
            result = result + str(a[i][j])
            j = j+1

    if j < len(a[i])-1:
        while j < len(a[i])-1:
            result=result+'9'
            j=j+1
    elif j == len(a[i]) - 1:
        result = result + str(a[i][j])
            
    result = int(result)
    ans.append(str(result))
            
        
print ans

file.close()
file = open(fout, "w")

for i in range(t):
    file.write("Case #"+str(i+1)+": "+ans[i]+'\n')
file.close()
