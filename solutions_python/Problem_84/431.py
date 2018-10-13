def solve(problem):
    wp = []
    answer = []
    rows = int(problem[0].split(" ")[0])
    cols = int(problem[0].split(" ")[1])
    #print (rows)
    #print (cols)
    flag = 0
    for i in range(1,rows+1):
        if (problem[i].count("#")%2 == 1):
            answer.append("Impossible") #Return at this point.            
            flag = 1
            break
    
    if(not flag):
        print (rows)
        for i in range(1,rows):
            print (i)
            x = 1; y = 1
            for j in range(0,cols):
                
                if(problem[i][j] == "#" and problem[i+1][j] == "#"):
                    tmp = list(problem[i]) 
                    if(x): 
                        tmp[j] = "/" 
                        x=0
                    else: 
                        tmp[j] = '*'
                        x = 1
                    problem[i] = "".join(tmp)
                    tmp = list(problem[i+1]) 
                    if(y): 
                        tmp[j] = "*" 
                        y=0
                    else: 
                        tmp[j] = "/"
                        y = 1
        
                    problem[i+1] = "".join(tmp)
                elif (problem[i][j] == "#" and problem[i+1][j] != "#"):
                    flag = 1
                    break 
        if(problem[rows].count("#") > 0):
            flag = 1
        if(flag):
            answer.append("Impossible")
        else:
            for i in range(1,rows+1):
                answer.append(problem[i])
    

    return answer

def actualsolve():
    with open('in.txt', 'r') as infile: # this will automatically close the file
            stuff = infile.readlines()
    
    print (stuff[0])
    ptr = 1

    for i in range(1,int(stuff[0])+1):
       
        instance = []
        for j in range(0,int(stuff[ptr].split(" ")[0])+1):
            if(stuff[ptr+j][-1:] == "\n"):
                instance.append((stuff[ptr+j][:-1]))
            else:
                instance.append((stuff[ptr+j][:]))
        print (instance)
        answer = solve(instance)
        ptr = ptr + int(stuff[ptr].split(" ")[0]) + 1
        print ("---------")
        print 
        print (answer)
        for x in answer:
            print(x)
        with open('out.txt', 'a') as scorefile:
            scorefile.write("Case #" + str(i) + ":\n")
            for x in answer:
                x = str(x)
                scorefile.write("{e}\n".format(e=x[0:14]))


actualsolve()


#p = ['4 5','.##..','.####','.####','.##..']
#p = ['4','.11.','0.00','01.1','.10.']
#p = ['3','.10','0.1','10.']
#solve(p)