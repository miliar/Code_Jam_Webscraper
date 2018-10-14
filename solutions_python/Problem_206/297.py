__author__ = 'sushrutrathi'

opt = open("output.txt", 'w')
with open("input.txt") as f:
    total_tests = int(f.readline())
    for tests in range(1,total_tests+1):
        d,n = [int(i) for i in f.readline().strip().split(' ')]
        ans = 0
        k = []
        s = []
        for i in range(n):
            K,S = [int(i) for i in f.readline().strip().split(' ')]
            k.append(K)
            s.append(S)

        time = (d-k[0])*1.0/s[0]

        for i in range(1,n):
            tim = (d-k[i])*1.0/s[i]
            time = max(tim,time)


        ans = d/time



        opt.write("Case #" + str(tests) + ": " + str(ans) + '\n')