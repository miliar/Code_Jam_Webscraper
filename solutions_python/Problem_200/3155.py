__author__ = 'sushrutrathi'

opt = open("output.txt", 'w')
with open("input.txt") as f:
    total_tests = int(f.readline())
    for tests in range(1,total_tests+1):
        s = f.readline().strip()
        for i in range(len(s)-1,0,-1):
            if s[i]<s[i-1]:
                s = s[0:i-1] + str(int(s[i-1])-1) + s[i:]
                for j in range(i,len(s)):
                    s = s[0:j] + '9' + s[j+1:]
        s = int(s)
        opt.write("Case #" + str(tests) + ": " + str(s) + '\n')