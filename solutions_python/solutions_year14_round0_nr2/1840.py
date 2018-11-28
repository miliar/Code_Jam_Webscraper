import sys

skip = True    

for i,l in enumerate(sys.stdin):
    if skip:
        skip = False
    else:
        C, F, X = map(float, l.split())
        x = 0
        rate = 2.0
        time = 0.0
        while True:
            a = X / rate
            b = (C - x) / rate
            if a > X / (rate + F) + b:
                time += b
                rate += F
            else:
                print 'Case #{}: {}'.format(i, time+a)
                break

