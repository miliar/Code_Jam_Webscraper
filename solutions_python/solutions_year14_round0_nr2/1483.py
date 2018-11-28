
def handle_output(C, F, X, caseno):
    rate = 2.0
    oldtime = float(X/rate)
    newtime = C/rate + X/(rate+F)
    rate = rate + F
    #print("---")

    while(newtime < oldtime):
        #print("O:",oldtime,"N:",newtime)
        oldtime = newtime
        newtime = newtime - (X/rate)
        newtime = newtime + (C/rate) + (X/(rate+F))
        rate = rate + F

    with open('output.txt', 'a') as fo:
        outstr = 'Case #'+ str(caseno) + ': ' + str(round(oldtime,7)) + '\n'
        fo.write(outstr)



with open('output.txt', 'w')as fo:
    pass

with open('input.txt') as fi:
    T = int(fi.readline())
    for t in range(1, T+1):
        inp1 = [float(x) for x in fi.readline().split(' ')]
        #print(inp1)
        C = inp1[0]
        F = inp1[1]
        X = inp1[2]
        handle_output(C,F,X,t)
