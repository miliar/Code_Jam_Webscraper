__author__ = 'Abhinav'
testcases = int(input())
for t in range(testcases):
    s,data = input().split()
    smax = int(s)
    data = list(map(int,data))
    count=data[0]
    add=0
    for k in range(1,len(data)):
        if count < k:
            add+=1
            count+=1
        count+=data[k]
    print('Case #{}: {}'.format(t+1,add))