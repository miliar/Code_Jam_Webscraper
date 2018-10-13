infile = open('input.txt','r')
outfile = open('output.txt','w')
lines = infile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
n = int(lines[0])
for i in range(n):
    k = int(lines[1+i*3])
    na = lines[2+i*3].split()
    ke = lines[3+i*3].split()
    for j in range(k):
        na[j] = float(na[j])
        ke[j] = float(ke[j])
    na = sorted(na)
    ke = sorted(ke)
    na1 = na[:]
    ke1 = ke[:]
    result = k
    for j in range(k):
        if na[0] < ke[0]:
            result = result - 1
            na = na[1:]
            ke = ke[:-1]
        else:
            na = na[1:]
            ke = ke[1:]
    res = k
    for j in range(k):
        for l in range (k):
            if ke1[l] > na1[j]:
                ke1[l] = 0
                res = res - 1
                break
    print 'Case #'+str(i+1)+': '+str(result)+" "+str(res)
    outfile.write('Case #'+str(i+1)+': '+str(result)+" "+str(res)+'\n')
