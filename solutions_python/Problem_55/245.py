with open('C-large.in') as input, open('out.txt', 'w') as output:
    cases = int(input.readline())
    for c in range(1,cases+1):
        case=input.readline().split(" ")
        R = int(case[0])
        k = int(case[1])
        groupStr = input.readline().split(" ")
        groups = []
        for str in groupStr:
            groups.append(int(str))
        profit = 0
        groupsize = len(groups)
        ridersets=[]
        riderIsets=[]
        found1 = False;
        found2 = False;
        found3 = False;
        foundIndex=0;
        lastR =R;
        index = 0
        
        for i in range(0,R):
            if not found3:
                riders = []
                riderIs = []
                numR =0
                while((len(groups)>0)&(numR<k)):
                    new = groups.pop(0)
                    numR += new
                    if(numR<=k):
                        riders.append(new)
                        index=index+1
                        riderIs.append(index%groupsize)
                        
                        
                    else:
                        groups.insert(0, new)
                        numR-=new
                        break
                
                if not riderIsets.__contains__(riderIs):
                    riderIsets.append(riderIs)
                    ridersets.append(riders)
                    profit+=numR
                else:
                    foundIndex = riderIsets.index(riderIs)
                    if found2:
                        found3=True
                    else:
                        if found1:
                            riderIsets.append(riderIs)
                            ridersets.append(riders)
                            profit+=numR
                            found2 = True
                        else:
                            riderIsets.append(riderIs)
                            ridersets.append(riders)
                            profit+=numR
                            found1 = True 
                groups.extend(riders)
               
            else:
                lastR = i-1
                break
        if lastR<R:
            perRepeat =0
            for set in range(foundIndex,len(ridersets)):
                for i in ridersets[set]:
                    perRepeat+=i
            profit += perRepeat*(int((R-lastR)/(len(ridersets)-foundIndex)))
            remainder = (R-lastR)%(len(ridersets)-foundIndex)
            for set in range(foundIndex,remainder+foundIndex):
                for i in ridersets[set]:
                    profit+=i
        print("Case #{}: {}".format(c,profit))
        output.write("Case #{}: {}\n".format(c,profit))