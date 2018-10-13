import math
def get_max_tidy(n):
    ns = str(n)
    if(len(ns)==1 or is_tidy(n)):
        return n
    else:
        for i in xrange(n-1,9,-1):
            if(is_tidy(i)):
                return i
            


def is_tidy(num):
    s = str(num);
    for i in range(len(s)-1):
        if s[i]> s[i+1]:
            return False
    return True


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {} ".format(i, get_max_tidy(n)))
