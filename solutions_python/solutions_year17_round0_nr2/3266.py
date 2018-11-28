
data = list()


for a in range(1, 10):
    for b in range(1,10):
        if a <= b :
            s = str(a)+str(b)
            data.append(int(s))
           # print(s)
for a in range(1,10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a<=b  and b<=c  or a ==b and b==c:
                S = str(a)+str(b)+str(c)
                S = int(S)
                #print(S)
                data.append(S)
                
            #print(c)
       # print(b)
    #print(a)

def StrCheck(test):
    if test == 10:
        return 9
    if test == 11:
        return 11

    if test == 1000:
        return 999
    
    if len(str(test))==1:
        return test
    if test ==data[len(data)-1]:
        return data[len(data)-1]
    if test < data[len(data)-1] and test >= data[len(data)-2]:
        return data[len(data)-2]

    for i in range(len(data)-1):
        if data[i] <= test:
            pass
        else:
            #print(data[i-1])
            return(data[i-1])
            print(i)
            break

t=int(input())


for cas in range(1,t+1):
    test=int(input())
    print ("Case #{}: {}".format(cas,StrCheck(test)))
