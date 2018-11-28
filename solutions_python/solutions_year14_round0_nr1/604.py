import sys

args = sys.argv

if len(args) < 2:
    print 'test or small or large?'
    exit()

inp = args[1]

out = open(inp + '_OUT', 'w')

def int_row():
    return map(int, raw_input().split())

# No change before this

def get_row(r):
    ret = None
    for i in xrange(1, 5):
        row = int_row()
        if r == i:
            ret = set(row)
    return ret

def solve():
    r = input()
    first = get_row(r)
    r = input()
    second = get_row(r)
    common = first.intersection(second)
    if len(common) == 0:
        return 'Volunteer cheated!'
    elif len(common) == 1:
        return str(list(common)[0])
    else:
        return 'Bad magician!'

T = input()
for i in xrange(1, T+1):
    ans = 'Case #' + str(i) + ': ' + solve()
    print ans
    out.write(ans + '\n')
# No change after this

out.close()
