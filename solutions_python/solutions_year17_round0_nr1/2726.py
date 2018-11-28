c=0
n = int(raw_input())
for m in range(n):
    r = raw_input().split()
    s = [g for g in r[0]]
    y = int(r[1])
    for i in range(len(s) - y + 1):
        if s[i] == "-":
            c += 1
            for j in range(i, i+y):
                if s[j] == "+":
                    s[j] = "-"
                else:
                    s[j] = "+"
    print "Case #" + str(m+1) + ":",
    for i in range(len(s) - y + 1, len(s)):
        if s[i] == "-":
            print "IMPOSSIBLE"
            break
    else:
        print c
            
    c = 0