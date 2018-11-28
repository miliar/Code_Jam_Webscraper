#!/usr/bin/python


n_tests = int(raw_input())

for test in range(n_tests):
    R,C = raw_input().split(" ")
    R = int(R)
    C = int(C)
    
    cake = []
    for i in range(R):
        cake.append(list(raw_input()))

    #step 1. Horizontal
    for i in range(R):
        pick = '?'
        for j in range(C):
            if cake[i][j] == '?':
                cake[i][j] = pick
            else:
                pick = cake[i][j]

        for j in range(C-1,-1,-1):
            if cake[i][j] == '?':
                cake[i][j] = pick
            else:
                pick = cake[i][j]


    #step 2. Vertical
    for j in range(C):
        pick = '?'
        for i in range(R):
            if cake[i][j] == '?':
                cake[i][j] = pick
            else:
                pick = cake[i][j]

        for i in range(R-1,-1,-1):
            if cake[i][j] == '?':
                cake[i][j] = pick
            else:
                pick = cake[i][j]
    

    print ("Case #"+str(test+1)+":")
    for i in range(R):
        s = ""
        for j in range(C):
            s = s+str(cake[i][j])
            
        print s
    
