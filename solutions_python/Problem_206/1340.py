t=int(input())
for i in range(1,t+1):
    d,n = map(int,input().split(' '))
    max_time = float(0)
    for j in range(n):
        k,s = map(float,input().split(' '))
        # print (d/(d-k)*s)
        if max_time < (d-k)/s:
            max_time=(d-k)/s
    max_speed = d/max_time

    # print (a,b,s)
    print("Case #{}: {}".format(i, max_speed))