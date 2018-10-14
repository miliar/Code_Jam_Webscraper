T = int(input())
for t in range(T):
    C,F,X = [float(elt) for elt in input().split()]
    time = 0
    rate = 2
    while(True):
        if(X/rate < C/rate + X/(rate+F)):
            print('Case #',t+1,': ',sep='', end='')
            print(format(X/rate + time,'.7f'))
            break
        else:
            time += C/rate
            rate += F
