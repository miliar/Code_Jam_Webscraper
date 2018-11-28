
testcases = int(input())
# print(testcases)

for testcase in range(1, testcases+1):
    n = int(input())
    a = list(map(float, input().split(" ")))
    b = list(map(float, input().split(" ")))
    eps = 10e-6

    a.sort()
    b.sort()

    
    normal_points = 0
    deceitful_points = 0
    tmp = b[:]
    # normal war:
    for i,el in enumerate(a):
        # naomi picks el

        # ken is picked by Ken
        bigger = [x for x in b if x > el]
        if bigger:
            ken = min(bigger)
        else:
            ken = b[0]
            normal_points += 1
        b.remove(ken)
    b = tmp
    # deceitful war:
    for i,el in enumerate(a):
        if el < b[0]:
            # tell ken we have max(b) - eps
            # he loses max(b) and gets a point
            b = b[:-1]
        else:
            # claim we have max(b) + eps
            b = b[1:]
            deceitful_points += 1

    print("Case #{}: {} {}".format(testcase, deceitful_points, normal_points))
