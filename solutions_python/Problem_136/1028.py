


testcases = int(input())
# print(testcases)

for testcase in range(1, testcases+1):
    line = input().split(" ");
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    t = 0
    v = 2
    while ( (v+f) * c < f * x):
        # buy a farm
        t += c / v
        v += f
    # final build up
    t += x / v
    print("Case #{}: {}".format(testcase, t))
    
