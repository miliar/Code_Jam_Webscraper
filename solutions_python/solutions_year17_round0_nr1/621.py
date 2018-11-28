t = input()
for poo in range(t):
    s, k = raw_input().split()
    k = int(k)
    count = 0
    s = [i for i in s]
    for i in range(len(s) - k + 1):
        if s[i] == '+':
            continue
        count += 1
        for j in range(k):
            s[i+j] = '+' if s[i+j] == '-' else '-'
    good = True
    for i in s:
        if i == '-':
            good = False
            break
    print "Case #" + str(poo+1) + ":", 
    if good:
        print count
    else:
        print "IMPOSSIBLE"
