def run():
    case = 1
    f = open("input.txt")
    f.readline()
    out = open("output.txt",'w')
    for line in f:
        test = line.strip()
        mx,inp = test.split(' ')
        friends=0
        people = 0
        for i in range(int(mx)+1):
            if people>=mx:
                #print("Breaking")
                break
            current=int(inp[i])
            #print("Current is: "+str(current))
            
            #print("People is: "+str(people))
            if people<i:
                friends+=i-people
                people+=i-people
                #print(str(i-people)+" friends needed")
            people+=current
            #print("Friends is: "+str(friends))
            
        out.write('Case #'+str(case)+': '+str(friends)+'\n')
        case+=1
        #print("New")
    f.close()
    out.close()
