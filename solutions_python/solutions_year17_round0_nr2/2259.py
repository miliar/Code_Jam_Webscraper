reader = open("C:\\Users\\saile\\OneDrive\\codejam2017\\Prob2\\input2.in", "r+")
output = open("C:\\Users\\saile\\OneDrive\\codejam2017\\Prob2\\output2.in", "r+")
reader = reader.read().split("\n")


for i in range(int(reader[0])):
    inp = [int(j) for j in list(reader[i+1])]
    print(inp)
    inp.reverse()
    curr = 0
    done = 0
    #231
    #921
    ite = 0
    print(inp)
    while not done:
        #print(curr, nex)
        
        if curr == len(inp) or ite == len(inp)-1:
            break
        
        if inp[ite+1]>inp[ite]:
            inp[curr] = 9
            inp[curr+1] -=1
            curr = curr+1
        else:
            ite+=1
        
    inp.reverse()
    print(int(''.join(map(str, inp))))
    output.write("Case #"+str(i+1)+": "+str(int(''.join(map(str, inp))))+"\n")
output.close()
