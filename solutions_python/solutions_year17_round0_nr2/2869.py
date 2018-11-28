T = int(input().strip())

for x in range(1, T+1):
    n = input().strip()
    
    if len(n) == 1:
        print("Case #{}: {}".format(x, n))
    else:        
        temp = list(n)
        i = 0
        ind = i
        while i < len(temp)-1 and temp[i+1] >= temp[i]:
            if temp[i+1] > temp[i]:
                ind = i+1
            i = i+1

        if ind < len(temp)-1:
            if temp[ind:].count(temp[ind]) == len(temp[ind:]):
                pass
            else:
                temp[ind] = str(int(temp[ind])-1)
                for j in range(ind+1, len(temp)):
                    temp[j] = '9'

        temp = "".join(temp)
        temp = int(temp)
        print("Case #{}: {}".format(x, temp))
