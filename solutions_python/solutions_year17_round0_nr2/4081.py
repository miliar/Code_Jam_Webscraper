def tidylarge(input):
    
    nomod = []
    while str(input) != ''.join(nomod):
        test = list(str(input))
        nomod = list(str(input))
        for i in range(len(test)):
            if i+1 == len(test):
                input = int(''.join(test))
                continue
            if int(test[i]) <= int(test[i+1]):
                continue
            else:
                test[i] = str(int(test[i])-1)
                for j in range(i+1,len(test)):
                    test[j] = '9'
    return int(''.join(nomod))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print('Case #%i: %i' % (i,tidylarge(n)))  