def next_it(C,F,X):
    CPS = 2
    S = 0
    while True:
        a = C/CPS
        b = X/CPS
        c = a + (X/(CPS+F))
        if b < c:
            return S + b
        else:
            S += a
            CPS += F

with open('data.in', 'r') as f:
    test_cases = int(f.readline())
    for i in range(test_cases):
        C,F,X = [ float(x) for x in f.readline().split(" ") ]
        print("Case #" + str(i+1) + ": " + str(next_it(C,F,X)))

        
