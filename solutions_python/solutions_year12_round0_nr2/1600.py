TESTCASE = input()

for testcase in range(1, TESTCASE+1):
    print ('Case #'+str(testcase)+':'),
    l = [int(x) for x in raw_input().split()]
    [N, S, p] = l[0:3]
    ans = 0
    for t in l[3:]:
        if t>=p:
            if (t-p)/2 >= p-1:
                ans += 1
            elif S > 0 and (t-p)/2 >= p-2:
                ans += 1
                S -= 1

    print ans
    
