input = open('test.in','r')
output = open('output.txt','w')
t = int(input.readline())
for i in range(1,t+1):
    size = int(input.readline())
    naomi = map(float,input.readline().split())
    ken = map(float,input.readline().split())
    naomi.sort()
    ken.sort()
    pos = 0
    count = 0
    for j in naomi:
        while pos < size:
            if j <= ken[pos]:
                pos += 1
                count += 1
                break
            pos += 1
    z = size-count
    pos = 0
    count = 0
    for j in ken:
        while pos < size:
            if j <= naomi[pos]:
                pos += 1
                count += 1
                break
            pos += 1
    y = count
    output.write("Case #"+str(i)+": "+str(y)+" "+str(z)+"\n")
output.close()
