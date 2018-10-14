T = int(input().strip())

for x in range(1, T+1):
    pan, k = input().strip().split(' ')
    k = int(k)
    pan = list(pan)
    count = 0
    i = 0
    while pan.count('+') != len(pan) and i <= len(pan)-k:
        if pan[i] == '-':
            count = count+1
            for j in range(i,i+k):
                if pan[j] == '-':
                    pan[j]='+'
                else:
                    pan[j]='-'
        i = i+1


    if pan.count('+') == len(pan):
        print("Case #{}: {}".format(x,count))
    else:
        print("Case #{}: IMPOSSIBLE".format(x))
     
    
