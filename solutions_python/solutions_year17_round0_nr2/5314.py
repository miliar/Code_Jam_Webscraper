t = int(input())
for i in range(1,t+1):
    data = input()
    dataNum = int(data)

    if len(data) == 1:
        print("Case #{0}: {1}".format(i,data))
    elif data == ''.join(sorted(data)):
            print("Case #{0}: {1}".format(i,data))
    else:
        finalNum = []
        j = 0
        while j+1<len(data) and data[j]<data[j+1]:
            finalNum.append(data[j])
            j += 1
        if j<len(data):
            finalNum.append(str(int(data[j])-1))

        appendData = '9'*(len(data)-len(finalNum))
        ans = ''.join(finalNum)+appendData
        print("Case #{0}: {1}".format(i,int(ans)))
