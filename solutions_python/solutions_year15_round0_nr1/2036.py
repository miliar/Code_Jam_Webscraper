from  sys import stdin, stdout
T = int(stdin.readline())
for c in range(T):
    case = stdin.readline().split()
    Smax = int(case[0])
    S = case[1]
    clapping = 0
    result = 0
    for i in range (Smax + 1):
        if(clapping < i):
            result += 1
            clapping += 1
        clapping += int(S[i])

    print "Case #{0}: {1}".format( c+1,  result)
