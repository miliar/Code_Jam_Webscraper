res = []

def process(C, F, X, rate):
    time = 0
    while True:
        if X <= C or C/rate + X/(rate + F) > X/rate:
            time += X/rate
            break
        else:
            time += C/rate
            rate += F
    return time
        
for i in range(input()):
    C, F, X = map(float, raw_input().split(' '))
    res.append(round(process(C, F, X, 2.0), 7))

for i in range(len(res)):
    print 'Case #' + str(i+1) + ': ' + str(res[i])
