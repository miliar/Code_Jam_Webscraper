


infile = open("A-small-attempt0.in","r")
line = infile.readline()
line = line.split()
N  = int(line[0])

for i in range(0,N):
    line = infile.readline()
    line = line.split()
    gln1 = int(line[0])-1
    gl1 = []
    for j in range(0,4):
        line = infile.readline()
        line = line.split()
        if(j == gln1):
            for k in range(0,len(line)):
                gl1.append(int(line[k]))
            
    line = infile.readline()
    line = line.split()
    gln2 = int(line[0])-1
    gl2 = []
    for j in range(0,4):
        line = infile.readline()
        line = line.split()
        if(j == gln2):
            for k in range(0,len(line)):
                gl2.append(int(line[k]))

    count = 0
    pr = []
    for j in range(0,len(gl1)):
        if (gl1[j] in gl2):
            count = count + 1
            pr.append(str(gl1[j]))

    result = ''
    if(count == 0):
        result = 'Volunteer cheated!'
    elif(count == 1):
        result = pr[0]
    else:
        result = 'Bad magician!'

    s = "Case #" + str(i+1) + ":"
    print s, result
        
