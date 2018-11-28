#!/usr/bin/python



def tidy(n):
    s = str(n)
    s = [int(s[i]) for i in range(len(s))]
    r = [int(s[i]) for i in range(len(s))]

    i = 0 
    while i < len(s)-1:
        if s[i+1] >= s[i]:
            r[i] = r[i]
            i = i + 1
        else:
            r[i] = (s[i]-1 )% 9
            i = i + 1
            j = i 
            while j < len(s):
                r[j] = 9
                j = j + 1
            break
    i = len(s) - 1
    while i > 0:
        if r[i] >= r[i-1]:
            r[i] = r[i]
            i = i - 1
        else:
            r[i] = 9
            i = i - 1
            r[i] = (s[i]-1) % 9
    res = 0
    for j in range (len (r)):
        res += pow(10, len(r)- j - 1 ) * r[j]
    return res


if __name__ == "__main__":
    t = int(input())
    for test in range(t):
        n = int(input())
        print "CASE #{}: {}".format(test+1, tidy(n))