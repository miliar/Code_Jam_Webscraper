
#reading file
with open("B-large.in") as z:
    casenumber = int(z.readline())
    
    #case!
    for case in range(1,casenumber+1):

    
        #reading file
        data1 = z.readline().strip().split(" ")
        data = str(data1[0])

        #this can be solved by some form of greedy too.
        #but care needs to be taken for numbers less than 111....1


        a = int(data)
        digits = len(data)



        check = 1
        for a0 in range(0,digits):
            if int(data[a0])>1:
                break
            elif data[a0]=="0":
                check=0
        if check==0:
            answer = 10**(digits-1)-1 #care has been taken
            
        else:
            answer = "0"
            position = -1
            ninesovertake = False
            chainofequals = 0
            while position!=digits-1 and ninesovertake==False:
                position+=1
                if int(data[position])>int(answer[-1]):
                    answer+=data[position]
                    chainofequals = 0
                elif int(data[position])==int(answer[-1]):
                    answer+=data[position]
                    chainofequals+=1
                else:
                    oops = int(answer[-1])
                    answer = answer[:-1-chainofequals] + str(oops-1)
                    stringofnines=""
                    for a0 in range(0,digits-position+chainofequals):
                        stringofnines+="9"
                    answer+=stringofnines
                    ninesovertake=True
            answer = answer[1:]
            
        print("Case #"+str(case)+": "+ str(answer))
            
        
