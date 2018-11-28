inp = open('input.txt').readlines()
op = open('output.txt','w')
t = int(inp[0])

for i in range(t):
    tem = inp[i+1].split()
    sMax = int(tem[0])
    arr = []
    for j in range(len(tem[1])):
        arr.append(int(tem[1][j]))

    for j in range(len(arr)):
        x = y = arr[j]
        if x>0:
            arr[j] = 1
            x = x-1
            while x>0 and j+y-x<len(arr) :
                arr[j+y-x] = arr[j+y-x]+1
                x = x-1
    count = 0
    for j in range(len(arr)):
        if arr[j]==0:
            count = count+1

    op.write("Case #"+str(i+1)+": "+str(count)+'\n')

op.close()
        
        
    
