#!/usr/bin/python



ntests = int(raw_input())

for test in range(ntests):
    s,k = raw_input().split()
    k = int(k)
    
    s = list(s)

    flips = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            for j in range(k):
                if s[i+j] == '-':
                    s[i+j] = '+'
                else:
                    s[i+j] = '-'
                    
            flips += 1
                

        for pk in s:
            if pk == '-':
                continue

    v = True
    for pk in s:
        if pk == '-':
            v = False

    print ("Case #"+str(test+1)+":"),
    if v:
        print flips
    else:
        print "IMPOSSIBLE"
        
