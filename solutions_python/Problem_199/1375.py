f = open('input.txt', 'r')
t = int(f.readline())

for i in range(t):
    c = 0
    b = False
    s, k = f.readline().split()
    sl = []
    for char in s:
        sl.append(char)
    k = int(k)
    for j in range(len(s)):
        if sl[j] == '+':
            continue
        for l in range(k):
            if j+k > len(sl):
                b = True
                break
            if sl[j+l] == '-':
                sl[j+l] = '+'
            else:
                sl[j+l] = '-'
        c += 1
    if b:
        print "Case #" + str(i + 1) + ": IMPOSSIBLE"
    else:
        print "Case #" + str(i+1) + ": " + str(c)
