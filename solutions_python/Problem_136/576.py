T = int(raw_input())

def solve(C, F, X):

    rate = 2.0
    time = 0.0
    
    while True:
        predict = time + (X/rate)
        time = time + (C/rate)
        rate = rate + F
        new = time + (X/rate)
        #print 'Predicted: ' + str(predict)
        #print 'Actual: ' + str(time)
        if(predict < new):
            return predict
        

for i in xrange(1, T+1):
    [C, F, X] = map(float, raw_input().split())

    print 'Case #' + str(i) + ': ' + str(solve(C,F,X))
