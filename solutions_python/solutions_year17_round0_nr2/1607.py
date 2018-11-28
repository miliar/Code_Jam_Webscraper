#! python
cases = int(raw_input())
for a in range(0, cases):
    snum = raw_input()
    s=list(snum)
    n = []
    for c in s:
        n.append(int(c))
    index = len(n) - 1
    while not (all(n[i] <= n[i+1] for i in xrange(len(n) - 1))):
        if n[index] != 0:
            n[index] = n[index]-1
        else:
            while n[index] == 0:
                n[index] = 9
                index = index - 1
            n[index] = n[index] - 1
    s = []
    for c in n:
        s.append(str(c))
    sout = ''.join(s)
    sout = sout.lstrip('0')
    print("Case #{}: {}".format(a+1, sout))
