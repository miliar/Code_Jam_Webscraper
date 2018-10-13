T= int(raw_input())
for t in range(T):
    s= raw_input()
    numbers=[]
    for ss in s:
        numbers.append(int(ss))
    index=25
    for i in range(len(numbers)-2,-1,-1):
        if numbers[i]>numbers[i+1]:
            index=i+1
            numbers[i]-=1
    rv=""
    #print index, numbers
    for i in range(len(numbers)):
        if i>=index:
            rv=rv+"9"
        else:
            if numbers[i]<0:
                rv=rv+"0"
            else:
                rv=rv+str(numbers[i])

    print "Case #%d: %d" % (t+1, int(rv))
