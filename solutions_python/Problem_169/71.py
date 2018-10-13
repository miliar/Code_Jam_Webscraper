inputF = open('B-small-attempt0.in', 'r')
output = open('B-small-attempt0.out', 'w')

numCases = int(inputF.readline())

def getFillTime(v,temp,hoses):
    if (temp > max(map(lambda x: x[1], hoses)) or
        temp < min(map(lambda x: x[1], hoses))):
        return -1

    if len(hoses) == 1:
        return v/hoses[0][0]

    elif hoses[0][1] == temp or hoses[1][1] == temp:
        if hoses[0][1] != temp:
            return v/hoses[1][0]
        elif hoses[1][1] != temp:
            return v/hoses[0][0]
        else:
            return v/(hoses[1][0] + hoses[0][0])

    elif len(hoses) == 2:
        v1 = v*(temp-hoses[0][1])/(hoses[1][1] - hoses[0][1])
        v0 = v-v1
        t0 = v0/hoses[0][0]
        t1 = v1/hoses[1][0]
        return max(t0, t1)
    

for i in range(numCases):
    spec = inputF.readline().split()
    numHoses = int(spec[0])
    v = float(spec[1])
    temp = float(spec[2])

    hoses = []
    for j in range(numHoses):
        line = inputF.readline().split()
        r = float(line[0])
        t = float(line[1])
        hoses += [(r,t)]

    time = getFillTime(v,temp,hoses)

    output.write('Case #' + str(i+1) + ': ')    
    if time < 0:
        output.write('IMPOSSIBLE\n')
    else:
        output.write(str(time) + '\n')




inputF.close()
output.close()
