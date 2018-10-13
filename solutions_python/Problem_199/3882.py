def flipPankes(arr,k):
    l = len(arr)
    count = 0
    while sum(arr)<l and count <100:
        count+=1
        i=0
        while arr[i]==1:
            i+=1
        #flip the next k bits:
        while i>(l-k):
            i-=1
        for j in range(i,i+k):
            if arr[j]==0:
                arr[j]=1
            else:
                arr[j]=0
    if count == 100:
        return 'IMPOSSIBLE'
    return count

inputfname ="A-small-attempt0.in" #"A-small-practice.in"
outputfname = inputfname+".out"
with open(inputfname,"r") as f:
    lines = f.readlines()
lines2 = [
'3',
'---+-++- 3',
'+++++ 4',
'-+-+- 4' ,      
]
n = int(lines[0].strip('\n'))
with open(outputfname,"w") as f:
     f.write('')
with open(outputfname,"a") as f:
    for i in range(1,n+1):
        arr_,k = lines[i].strip('\n').split(' ')
        k = int(k)
        arr = []
        for c in arr_:
            if c=='+':
                arr.append(1)
            else:
                arr.append(0)
        #print arr,k
        outstring = 'Case #'+str(i)+': '+str(flipPankes(arr,k))
        #print outstring
        f.write(outstring+"\n")