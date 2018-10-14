input = file("input.txt")
output = file("output.txt", "w")
result = []

temp = input.readline().split();
l,d,n=[int(i) for i in temp]
dictionary=[{} for i in range(l)]
for i in range(d):
    temp = list(input.readline())[:-1]
    for j in range(l):
        if temp[j] not in dictionary[j] :
            dictionary[j][temp[j]]=[]
        dictionary[j][temp[j]].append(i)

for i in range(n):
    count = [([0]*l)for q in range(d)]
    temp = list(input.readline())[:-1]
    
    brace = False
    cursorcount = 0
    for char in temp:
        if char is '(':
            brace = True
            continue
        if char is ')':
            brace = False
            cursorcount += 1
            continue
        for k in dictionary[cursorcount].get(char, []):
            count[k][cursorcount] = 1
        if not brace:
            cursorcount += 1
        
    sum = 0
    for j in count:
        isword = True
        for h in j:
            if h == 0:
                isword = False
                break
        
        if isword:
            sum+=1
    result.append(sum)

for i in range(n):
    print >> output, "Case #%d: %d" % ((i+1), result[i])
    
input.close()
output.close()