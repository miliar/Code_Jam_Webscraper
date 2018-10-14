def func(j, s):
    for i in xrange(j+1):
        s[i] = 9

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    l = list(str(n))

    if(all(l[i] <= l[i+1] for i in xrange(len(l)-1))):
        a = str(n)

    else:
        l.reverse()
        l = map(int, l)
        for j in xrange(len(l)-1):
            if l[j] < l[j+1]:
                l[j+1] -= 1
                func(j, l)
        if l[len(l)-1] == 0:
            l.pop()
        l.reverse()
        l = map(str, l)
        a = ''.join(l)
        #a = l

    print("Case #"+str(i)+": "+a)
