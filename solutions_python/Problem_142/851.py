


from bisect import bisect_right,bisect_left

class GetOutOfLoop( Exception ):
     pass
 
inFile = open("A-small-attempt0.in")
outFile = open("test.out","w")

T = inFile.readline()
T = int(T)

for num in range(0,T):
    
    flag = 0
    N = int(inFile.readline())
    strN = []
    totalMoves =0
    #N lines in strN
    try:
        for i in range(0,N):
            counts = [0] * N
            line = inFile.readline();
            strN.append(line);
        
        while 1:
            C = "" 
            
            if len(strN[0]) <= 0:
                flag = 2;
                raise GetOutOfLoop
            C = strN[0][0]          #set current processing character
            for i in range(0,N):
                pointer = 0
                while 1:
                    
                    if (pointer >= len(strN[i])):
                        if pointer == 0:
                            flag = 1
                            raise GetOutOfLoop   
                        else:
                            counts[i]=pointer
                            strN[i] = strN[i][pointer:]
                            break             
                    
                    elif (strN[i][pointer] == C):
                        pointer+=1
                    
                    else:
                        if pointer == 0:
                            flag = 1
                            raise GetOutOfLoop   
                        else:
                            counts[i]=pointer
                            strN[i] = strN[i][pointer:]
                            
                            break
            #if C != '\\n':
            avg = 0
            total = 0
            med = 0
            for k in range(0,N):
                total+=counts[k];
            avg = total/N 
            dif = abs(counts[0] - avg)
            for k in range(1,N):
                td = abs(counts[k] - avg)
                if td < dif:
                    med = k
            
            for k in range(0,N):
                totalMoves += abs(counts[med] - counts[k]) 
                       
    except GetOutOfLoop:
        pass 
                
    if flag == 1:
        outFile.write("Case #"+str(num+1)+": Fegla Won\n")
    else:
        ff = 0
        for i in range(0,N):
            if (len(strN[i]) != 0):
                ff = 1
                break
        if ff == 1:
             outFile.write("Case #"+str(num+1)+": Fegla Won\n")
        else:
            outFile.write("Case #"+str(num+1)+": "+str(totalMoves)+"\n")
            
            
    #else:
        #outFile.write("Case #"+str(num+1)+": "+str(countD)+" "+str(countN)+"\n")

inFile.close();
outFile.close();