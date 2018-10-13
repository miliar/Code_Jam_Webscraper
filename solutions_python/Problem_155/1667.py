test = int(input())
for it in range(test):
    string = input().strip().split()
    smax = int(string[0]) + 1 
    string = list(map(int,list(string[1])))
    invite = 0
    sum = 0
    for i in range(smax):
        if i<=sum:
            sum+=string[i]
        else:
            invite += i-sum
            sum+= string[i] + i - sum
    print('Case #',it+1,': ',invite,sep='')

