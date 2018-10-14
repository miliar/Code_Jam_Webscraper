for tt in range(int(input())):
    a, b, k = map(int, input().split())
    r = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                r += 1
    print ("Case {}: {}".format(tt+1,r))
                
