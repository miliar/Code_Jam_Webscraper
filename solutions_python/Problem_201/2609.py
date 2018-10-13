def check_max(stalls):
    maxS = 0
    startI, endI = 0, 0

    index = 0
    while index < len(stalls):
        tempS, tempM = index, 0
        while stalls[index] == '':
            tempM += 1
            index += 1
            if index == len(stalls):
                break
            
        tempE = index
        if tempM > maxS:
            maxS = tempM-1
            startI = tempS
            endI = tempE-1
            
        index+=1
    return startI, endI

def check_space(stalls, index):
    Ls, Rs = 0, 0
    temp = index
    while stalls[temp+1] == '':
        Rs += 1
        temp += 1

    temp = index
    while stalls[temp-1] == '':
        Ls += 1
        temp -= 1
    
    return Rs, Ls

infile = open("C-small-1-attempt0.in", "r")
outfile = open("C-small.out", "w")

t = infile.readline()
print(t)
casenumber = 1

for line in infile:

    n, k = line[:-1].split()
    n = int(n)
    k = int(k)
    stalls = ['x']+['' for x in range(int(n))]+['x']
    
    for i in range(k):
        startI, endI = check_max(stalls)
        mid = (startI + endI) // 2
        stalls[mid] = 'x'
        
    Rs, Ls = check_space(stalls, mid)
    
    maxS = max(Rs, Ls)
    minS = min(Rs, Ls)
    
    
    print("Case #{}: {} {}".format(casenumber, maxS, minS), file=outfile)
    casenumber+=1

print("done")
infile.close()
outfile.close()
    
