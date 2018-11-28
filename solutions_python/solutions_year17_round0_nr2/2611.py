def solve_b(path="E:\\Users\\Neta\\Desktop\\dashyts\\googlejam.txt"):
    f = open(path, "r")
    T = f.readline()
    T = int(T)
    #path_out = "E:\\Users\\Neta\\Desktop\\dashyts\\googlejamSOL.txt"
    #fout = open(path_out, "w")
    case = 0
    for i in range(T):
        line = f.readline()
        case = case + 1
        count = 1
        bound = int(line)
        #print("bound: " + str(bound))
        #print("starting first phase")
        while(count <= bound):
            if(count * 10 + 1 <= bound):
                count = count * 10 + 1
            else:
                break
            #print("count: " + str(count))
        standard = count
        #print("starting second phase")
        while(count <= bound):
            #print("count: " + str(count))
            #print("standard: " + str(standard))
            if(count + standard > bound):
                standard = int(standard / 10)
                continue
            if (standard == 0):
                break
            if (count + standard)%10 == 0:
                break
            count = count + standard
        print("Case #" + str(case) +": "+ str(count))
