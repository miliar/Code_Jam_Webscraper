# cook your code here
for case in xrange(int(raw_input())):
    n = raw_input()
    a = ''
    for i in xrange(len(n) - 1, 0, -1):
        if n[i] < n[i - 1]:
            n = n[0:i-1] + str(int(n[i - 1]) - 1) + ('9' * (len(n) - i))
    n = int(n)
    print "Case #" + str(case + 1) + ":", n