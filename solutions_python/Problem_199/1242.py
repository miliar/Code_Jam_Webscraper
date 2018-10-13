t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    S, K = raw_input().split(" ")
    K = int(K)
    
    l = list(S)
    n = len(S)
    curr = 0
    cnt = 0

    while '-' in l:
        ind = curr + l[curr:].index('-')
        # print ind 
        if ind + K > n:
            break

        for j in range(ind, ind+K):
            l[j] = '-' if l[j] == '+' else '+'
        # print l

        cnt += 1
        curr = ind
    
    if '-' in l:
        print "Case #{}: IMPOSSIBLE".format(i)
    else:
        print "Case #{}: {}".format(i, cnt)
        

