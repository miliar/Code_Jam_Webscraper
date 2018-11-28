

def cookie_clicker(C,F,X):
    rate = 2;
    current_wait =float(0)
    for i in xrange(10000000):

        ifwait = (C/rate)+(X/(rate+F))
        nowait = X/(rate)
        if ifwait< nowait:
            current_wait +=C/rate
            rate += F
        else:
            current_wait +=nowait
            break
    return current_wait


T=int(raw_input())
solutions = []
for t in xrange(T):
    three = map(float, raw_input().strip().split())
    C = three[0]
    F = three[1]
    X = three[2]
    
    sol = cookie_clicker(C,F,X)
    form = "Case #%d: %8f" %(t+1, sol)
    solutions.append(form)

with open('cookie_ouput.txt', 'w') as f:
    for s in solutions[:-1]:
        f.write(s)
        f.write("\n")
    f.write(solutions[-1])