file = open("C-small-1-attempt0.in","r")
lines = file.readlines()[1:]
file.close()

temp = []
results = []

def addStalls():
    global stalls
    curr = max(stalls)
    index = stalls.index(curr)
    if curr%2!=0:
        stalls = stalls[:index]+[curr//2,0,curr//2]+stalls[index+1:]
        return [curr//2,curr//2]
    else:
        stalls = stalls[:index]+[curr//2-1,0,curr//2]+stalls[index+1:]
        return [curr//2,curr//2-1]

for line in lines:
    [n,k] = line.split(" ")
    n,k = int(n),int(k)
    if n==k:
        temp.append([0,0])
    else:
        stalls = [0,n,0]
        for i in range(k-1):
            addStalls()
        temp.append(addStalls())

file = open("C-small-1-attempt0.out","w")
for i in range(len(temp)):
    results.append("Case #{0}: {1} {2}\n".format(i+1,temp[i][0],temp[i][1]))
file.writelines(results)
file.close()
