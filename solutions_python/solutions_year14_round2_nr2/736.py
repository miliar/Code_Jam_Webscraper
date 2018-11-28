t = int(input())
t1=1
while t1<=t :
    l = list(map(int,input().split(" ")))
    a = l[0];b=l[1];k=l[2]
    count = 0
    for i in range(a):
        for j in range(b):
            if (i&j) < k:
                count+=1
    print('Case #{}: {}'.format(t1,count))
    t1+=1
