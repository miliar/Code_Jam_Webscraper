from decimal import Decimal as D
from decimal import *
getcontext().prec = 9

filename = 'B-large'
inputfile = filename + '.in'
outputfile = filename + '.out'

def do_buy(CF, current_cookies, C, F, X):
    assert current_cookies >= C
    # print CF, current_cookies, C, F, X
    # print (X - current_cookies)/CF, (X - current_cookies + C)/(CF + F)
    if (X - current_cookies)/CF < (X - current_cookies + C)/(CF + F):
        # print "False"
        return False
    # print "True"
    return True

with open(inputfile) as input, open(outputfile, 'w') as output:
    T = int(input.readline())
    for j in xrange(T):
        CF = D("2.0")
        current_cookies = D("0.0")
        # cost, frequency, goal
        C, F, X = map(D, input.readline().split())
        time = 0
        while current_cookies < X:
            # print "time", time
            if current_cookies == C:
                if do_buy(CF, current_cookies, C, F, X):
                    current_cookies = 0
                    CF += F
                else:
                    time += (X - current_cookies)/CF
                    current_cookies = X
            elif current_cookies == 0:
                current_cookies = min(X, C)
                time += min(X, C) / CF
                # if (X/CF) <= (C/CF + X/(CF + F)):
                #     time += X / CF
                #     current_cookies = X
                # else:
                #     time += (C - current_cookies)/CF
                #     current_cookies = C
            else: assert False
        output.write("Case #{t}: {time}\n".format(t=j+1, time=time))
