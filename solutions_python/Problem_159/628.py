__author__ = 'alex'


tests = input()

for test in range(int(tests)):
    n = input()
    l = list(map(int, input().split()))
    v1 = 0
    v2 = 0
    ms = 0

    for i in range(0, len(l)-1):
        v1 += max(l[i]-l[i+1], 0)
        ms = max(l[i]-l[i+1], ms)

    for i in range(0, len(l)-1):
        v2 += min(l[i], ms)

    print("Case #"+str(test+1)+": "+str(v1)+" "+str(v2))

