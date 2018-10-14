## Google CodeJam 2017-04-08 
## Problem B: "Tidy numbers" 
## @author Ylva Jansson

def get_tidy(n):
    nstr = str(n)
    ndigits = len(nstr)
    last_ok = 0
    
    previous = nstr[0]
    tidy = True
    for i in range(1, ndigits):
        current = nstr[i]
        if previous <= current:
            last_ok += 1
            previous = current
        else:
            tidy = False
            break
    if tidy:
        return n
    else:
        closest = nstr[0:last_ok] + str(int(nstr[last_ok])-1) + "9"*(ndigits-last_ok-1)
     #   print("closest", closest)
        return get_tidy(int(closest))

def get_all_tidy(T):
    res = [None]*len(T)
    for (i,t) in enumerate(T):
        res[i] = get_tidy(t)
    return res

# Read input
nT = int(input())  # read a line with a single integer
T = [None]*nT
for i in range(nT):
    T[i] = int(input()) # read a single integer
    
res = get_all_tidy(T)


for i in range(1,len(T)+1):
    print('Case #' + str(i) + ": " + str(res[i-1]))
