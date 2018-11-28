def isTidy(n):
    s = str(n) # convert to string.
    for i in range(0,len(s) - 1):
        if s[i] > s[i+1]:
            return False
    return True


def makeTidy(n):
    s = str(n) # convert to string.

    for i in range(0,len(s) - 1):
        if s[i] > s[i+1]:
            return n - (int( s[i+1:]) + 1)
    return n
T = int(raw_input()) # number of test cases

for i in range(0, T):
    # Number we want to check if it is tidy. 
    n = int(raw_input())
    solString = "Case #" + str(i+1) +":  "
    while not isTidy(n):
        n = makeTidy(n)
    print solString +  str(makeTidy(n))

#~ print isTidy(129)
#~ print makeTidy(132)
