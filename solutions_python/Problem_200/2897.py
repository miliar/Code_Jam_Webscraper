t = int(input())

for cas in range(t):
    n = list(input())

    lastchange = len(n)
    for i in range(len(n) - 1, 0, -1):
        if n[i - 1] > n[i]:
            n[i - 1] = chr(ord(n[i - 1]) - 1)
            lastchange = i;

    for i in range(lastchange, len(n)):
        n[i] = '9'

    print("Case #%d: %s" % (cas + 1, int("".join(n))))
