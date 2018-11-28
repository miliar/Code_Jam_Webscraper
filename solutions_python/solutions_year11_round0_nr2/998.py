file=open('testin5.txt')
out=open('output.txt','w')
T = int(file.readline())
for i in range(0,T):
    line = file.readline()
    info = line.split(" ")
    C = int(info[0])
    combos=dict()
    conflicts = []
    index = 1
    for j in range(0,C):
        com = info[index]
        comkey = list(com[0:2])
        comkey.sort()
        key = ''
        for l in comkey:
            key=key+l
        combos[key]=com[2]
        index=index+1
    D = int(info[index])
    index=index+1
    for k in range(0,D):
        conf = list(info[index])
        conf.sort()
        con = ''
        for l in conf:
            con=con+l
        conflicts.append(con)
        index=index+1
    inputs = info[index+1]
    output = []
    for letter in inputs:
        if letter!='\n':
            output.append(letter)
            if len(output)>1:
                lasttwo = output[len(output)-2:len(output)]
                lasttwo.sort()
                ltwo = ''
                for l in lasttwo:
                    ltwo=ltwo+l
                #print(ltwo)
                if ltwo in combos.keys():
                    output=output[0:len(output)-2]
                    output.append(combos[ltwo])
                else:
                    for x in output:
                        a=[]
                        a.append(x)
                        a.append(letter)
                        a.sort()
                        newkey = ''
                        for l in a:
                            newkey = newkey+l
                        if newkey in conflicts:
                            output=[]
                            break                    
        #print(output)
##    print(combos)
##    print(conflicts)
##    print(inputs)
    out.write('Case #')
    out.write(str(i+1))
    out.write(': ')
    out.write('[')
    index = 1
    for l in output:
        out.write(l)
        if index<len(output):
            out.write(', ')
        index=index+1
    out.write(']')
    out.write('\n')
out.close()
file.close()
