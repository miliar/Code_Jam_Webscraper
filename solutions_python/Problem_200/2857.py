#!/usr/bin/env python

def case(T):
    s = input()
    a = list(map(int, s))
    a = tidy(a)
    return "".join(map(str,a))

def correct(a):
    return sorted(a) == a

def tidy(a):
    m = 0
    for i in range(len(a)):
        if a[i] < m:
            for j in range(i, len(a)):
                a[j] = 9
            a = list(map(int,str( int("".join(map(str,a))) - 10**(len(a)-i)   )))
            a = tidy(a)
            break
        else:
            m = a[i]
    return a


if __name__=="__main__":
    for i in range(int(input())):
        print("Case #{}: {}".format(i+1, case(i)))
