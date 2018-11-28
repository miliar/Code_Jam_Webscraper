import fileinput,sys
A = sys.argv
if len(A) != 3:
    print("Usage: python3 [I-file] [O-file]")
    sys.exit()
array,case,output = [],0,open(A[2],'w')
for line in fileinput.input(A[1]): array += [line[:-1].split(' ')[1:]]
array = array[1:]
for i in array:
    b,o,c,pB,pO,t = [],[],[],1,1,0
    case += 1
    for j in range(0,len(i),2):
        if i[j] == 'B': b += [int(i[j+1])]
        else: o += [int(i[j+1])]
        c += [i[j]]
    while len(c):
        if b:
            if c[0] == 'B' and pB == b[0]: b,c[0] = b[1:],'X'
            elif pB > b[0]: pB -= 1
            elif pB < b[0]: pB += 1
            else: pass
        if o:
            if c[0] == 'O' and pO == o[0]: c,o = c[1:],o[1:]
            elif pO > o[0]: pO -= 1
            elif pO < o[0]: pO += 1
            else: pass
        if c and c[0] == 'X': c = c[1:]
        t += 1
    output.write('Case #'+str(case)+': '+str(t)+'\n')
