def solve(x, r, c):
    if x == 1:
        return True
    if x == 2:
        return (r * c) % 2 == 0
    if x == 3:
        return (r * c) % 3 == 0 and r * c >= 6
    if x == 4:
        return (r * c) % 4 == 0 and r * c >= 12

testcase_count = int(input())
for testcase_index in range(testcase_count):
    testcase_data = input().split()
    x = int(testcase_data[0])
    r = int(testcase_data[1])
    c = int(testcase_data[2])
    solvable = solve(x, r, c)
    print("Case #%d: %s" % (testcase_index + 1, "GABRIEL" if solvable else "RICHARD"))
    
