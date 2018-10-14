testcase = int(input())

for tc in range(1, testcase+1):

    t = int(input())
    t_save = t
    tlist = []
    while(t>0):
        tlist.append(t%10)
        t = t // 10

    #print(tlist)
    tlist.reverse()

    '''
    prevcompare = 0
    comparestatus = [] # [i] : compare [i] vs [i+1]
    for i in range(len(tlist) - 1):
        if tlist[i] < tlist[i+1]:
            comparestatus.append(1)
        elif tlist[i] == tlist[i+1]:
            comparestatus.append(0)
        else:
            comparestatus.append(1)
    '''
    #print(tlist)
    superstatus = True
    i = 0
    while i < len(tlist) - 1:
        #print(i, tlist)
        if tlist[i] <= tlist[i+1]:
            i += 1
            continue
        else:
            '''
            if i==0 and tlist[0] == 1:
                superstatus = False
                break
            '''
            tlist[i] -= 1
            for j in range(i+1, len(tlist)):
                tlist[j] = 9

            if i>0:
                i -= 1
            elif tlist[0] < 1:
                if i==0:
                    superstatus = False
                    break
                
            '''
            if i>0 and tlist[i] < 1:
                i -= 1
            elif i==0 and tlist[i] < 1:
                superstatus = False
                break
            else:
                i += 1
            '''
    #print(tlist)
    
    if superstatus:
        ans = ""
        for i in range(len(tlist)):
            ans += str(tlist[i])
        print("Case #"+str(tc)+": "+str(ans))
    else:
        ans = ""
        for i in range(len(tlist)-1):
            ans += "9"
        print("Case #"+str(tc)+": "+str(ans))
