T = int(input())
for t in range(0,T):
    number = int(input())
    tidy = '-1'
    nString = str(number)
    N = len(nString)
    tidy = number
    if N>1:
        prev = int(nString[0])
        for i in range(0,len(nString)):
            curr = int(nString[i])
            if prev > curr:
                if prev == 1 and curr == 0:
                    tidy = '9'*(len(nString)-1)
                else:
                    nend = len(nString[i:])
                    end = '9'*nend
                    start = str(int(nString[:i])-1)
                    tidy = int(start + end)
                break
            else:
                prev = curr
        stidy = str(tidy)
        prev = int(stidy[0])
        for i in range(0,len(stidy)):
            curr = int(stidy[i])
            if prev > curr:
                if prev == 1 and curr == 0:
                    #print('fixing '+stidy)
                    tidy = '9'*(len(stidy)-1)
                    #print('fixed'+str(tidy))
                else:
                    #print('fixing '+stidy)
                    nend = len(stidy[i:])
                    end = '9'*nend
                    start = str(int(stidy[:i])-1)
                    tidy = int(start + end)
                    #print('fixed'+str(tidy))
                break
            else:
                prev = curr

    stidy = str(tidy)
    prev = stidy[0]
    for ch in stidy:
        if int(prev) > int(ch):
            print("*******Ooopss...Case #{}: {} : {}".format(t+1,number,stidy))
            break
        prev = ch
            #print(stidy)
    print("Case #{}: {}".format(t+1,tidy))
