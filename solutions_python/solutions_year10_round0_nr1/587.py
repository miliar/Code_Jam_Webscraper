#!/usr/bin/python

T = int(raw_input(""))
output = []
for t in xrange(T):
    n, k = raw_input("").split()
    n = int(n)
    k = int(k)
    if k % 2**n == 2**n - 1:
        state = "ON"
    else:
        state = "OFF"
    output.append("Case #%d: %s" % (t+1, state))

for k in output:
    print k
