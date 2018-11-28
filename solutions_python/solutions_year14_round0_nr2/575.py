fin = open('B-large.in.txt','r')

fout = open('output.txt', 'w')

numCases = int(fin.readline())

for cases in range(numCases):
    data= [float(x) for x in fin.readline().split()]
    C = data[0]
    F = data[1]
    X = data[2]

    t = X/2
    num = 0
    while True:
        tempTime = t + C/(2+num*F) - X/(2+num*F) + X/(2+(num+1)*F)
        if tempTime > t:
            break
        else:
            t = tempTime
        num = num+1


    fout.write("Case #" + str(cases+1) + ": "+str(t)+'\n')

fin.close()
fout.close()