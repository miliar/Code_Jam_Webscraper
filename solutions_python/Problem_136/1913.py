import sys

# How many cases?
def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        loop(case)

def loop(case):
    inp = sys.stdin.readline().split(' ')
    inp = [float(x) for x in inp]
    
    C = inp[0] # required amount of cookie to buy a farm
    F = inp[1] # bonus rate of cookies get per second (increased for each farm owned )
    X = inp[2] # Goal
    R = 2.0    # (initial) rate of cookies get per second
    
    T = []     # Time variable
    TX = []    # Time to reach goal by waiting; index = amount of farm owned
    TC = [] # Time needed to buy farm
    
    resTX = resTC = 0.0
    c = 0
    while True:
        # Calculate time to reach goal w/o buying farm and time to buy a farm
        TX.append(X/R)
        TC.append(C/R)
    
        # If TX > TR, buy farm, else, stop; limit c to 4000
        if TC[-1] < TX[-1] and c < 4000:
            R = R + F
            c += 1
        else:
            break
    
    # Calculate every possible time
    for i in range(0,len(TX)):
        resTC = 0
        for n in range(0, i):
            resTC = resTC + TC[n]
        resTX = TX[i]
        resT = resTX + resTC
        T.append(resT)
    
    # Sort time needed
    T.sort()
    
    # Print lowest time; rounded to 7 decimal places
    sys.stdout.write("Case #{}: {}\n".format(case, str(round(T[0],7))))
    

if __name__ == '__main__':
    main()
    
    