def PbB(Input):
    f = open(Input)
    T = f.readline()
    T = int(T.rstrip('\n'))
    # print(T==4)
    out = open("output.txt",'w')
    count = 1
    for line in f:
        N = line.rstrip('\n')
        #print(N)
        flag = False;
        while flag == False:
            if len(N) == 1:
                flag = True
            else:
                for k in range(len(N)-1):
                    if int(N[k])>int(N[k+1]):
                        flag = False
                        N = N[0:k]+str(int(N[k])-1)+ '9'*(len(N)-k-1)
                        if N[0]=='0':
                            N = N[1:]
                        
                        break
                    flag = True
        #print("New N: "+N)
        out.write('Case #'+str(count)+': '+str(N)+'\n')
        count = count+1

    out.close()
        
