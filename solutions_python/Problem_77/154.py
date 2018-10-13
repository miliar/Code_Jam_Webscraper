
def GoroSort():
    raw_input()
    count, i = 0, 1
    for n in map(int, raw_input().split()):
        if n != i:
            count += 1
        i += 1
    print count

#---------------------------------------------------------------

T = int(raw_input())
for testcase in range(T):
    print "Case #%d:" % (testcase+1),
    GoroSort()
