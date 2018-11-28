def ints(): return map(int, raw_input().split())
T, = ints()
def get_row():
    r = int(raw_input()) - 1
    ans = None
    for i in range(4):
        row = set(ints())
        if r == i:
            ans = row
    return ans

def solve():
    x = get_row()
    y = get_row()
    opts = x.intersection(y)
    if opts:
        if len(opts) > 1:
            return "Bad magician!"
        else:
            return list(opts).pop()
    else:
        return "Volunteer cheated!"

for case_num in range(1, T+1):
    print "Case #%d: %s" % (case_num, solve())
