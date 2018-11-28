a = int(input())
for value in range(1,a+1):
    b = input().split()
    c = int(b[0])
    d = int(b[1])
    p = [0] * (c + 2)
    p[0] = 1
    p[-1] = 1
    #print(p)
    for value2 in range(d):
        mindisl = 0
        mindisr = 0
        posi = 10000
        for value3 in range(1,c+1):
            if p[value3] == 1:
                pass
            else:
                rcount = 0 
                for i in range(value3+1,c+1):
                    if p[i] == 1:
                        break
                    rcount += 1
                lcount = 0 
                for i in range(value3-1,-1,-1):
                    if p[i] == 1:
                        break
                    lcount += 1
                if min(lcount,rcount) > min(mindisl,mindisr):
                    posi = value3
                    mindisl = lcount
                    mindisr = rcount
                elif min(lcount,rcount) == min(mindisl,mindisr):
                    if max(lcount,rcount)  > max(mindisl,mindisr):
                        posi = value3
                        mindisl = lcount
                        mindisr = rcount
                    elif  max(lcount,rcount)== max(mindisl,mindisr):
                        if value3 < posi:
                            posi = value3
                            mindisl = lcount
                            mindisr = rcount
        p[posi] = 1
    #print(p)
    print("Case #"+ str(value) + ":",max(mindisl,mindisr),min(mindisl,mindisr))
