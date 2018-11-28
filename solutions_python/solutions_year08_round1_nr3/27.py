def solve(n):
    t = ['001', '005', '027', '143', '751', '935', '607', '903', '991', '335', '047', '943', '471', '055', '447', '463', '991', '095', '607', '263', '151', '855', '527', '743', '351', '135', '407', '903', '791', '135', '647'] # values
    return t[n]

def read_input():
    from sys import stdin
    C = int(stdin.readline())
    for c in range(C):
        print "Case #%d: %s" % (c+1, solve(int(stdin.readline())))

read_input()
