#!/usr/bin/python

def make_tidy(bound):
    a = []
    for i in range(1,10):
        a.append(i)
    i = 0
    while (i < len(a) and a[i] < bound):
        # print "i = ", i
        num = a[i]
        last = num % 10
        for j in range(last, 10):
            a.append(10 * num + j)
        i += 1
    return a

if __name__ == "__main__":
    t = int(raw_input())
    bound = 1000000000000000000L
    a = make_tidy(bound)
    # print "len(a) = ", len(a)
    for i in range(0, t):
        N = int(raw_input())
        j = 0
        while a[j] <= N:
            j += 1
        print "Case #" + str(i+1) + ":", a[j - 1]
            
