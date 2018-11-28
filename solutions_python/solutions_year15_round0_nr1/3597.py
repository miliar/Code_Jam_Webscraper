fob=open('A-small-attempt2.in','r')
caseNum=int(fob.readline())


for x in range(0,caseNum):
    case=fob.readline()
    case_list=list(case)
    max_shy=int(case_list[0])
    friend = 0
    if(max_shy == 0):
        print("case #"+str(x+1)+": "+str(friend))
        continue
    else:
        
        for z in range(2,len(case_list)-1):
            total = 0
            if(int(case_list[z]) != 0):
                for a in range(2,z):
                    total = int(case_list[a]) + total
                total1 = total + friend
                if(total1 <= z-2):
                    friend = friend + (z-2-total1)
        print("case #"+str(x+1)+": "+str(friend))
        
