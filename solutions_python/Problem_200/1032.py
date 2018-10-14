T = int(raw_input())
for x in xrange(1, T + 1):
    n = raw_input()
    print("Case #{}:".format(x)),
    if len(n) is 1:
        print(n)
        continue
    if ''.join(sorted(n)) == n:
        print(n)
        continue
    printed = False
    i = 1
    while(i is not len(n)):
        if n[i] < n[i - 1]:
            r = int(n[i:]) + 1
            n = str(int(n) - r)
            i = 0
        i += 1
    if printed is False:
        print(n)
