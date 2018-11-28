import sys

args = sys.argv

if len(args) < 2:
    print 'small or large?'
    exit()

inp = args[1]

out = open(inp + '_OUT', 'w')

# No change before this

def check_win(s, player):
    if s.count(player) == 4:
        return True
    if s.count(player) == 3 and s.find('T') >= 0:
        return True
    return False

def solve():
    ans = 0
    m, s = raw_input().strip().split()
    standing = 0
    # print s
    for needed, count in enumerate(s):
        count = int(count)
        # print needed, standing, count
        if count > 0:
            if needed > standing:
                diff = needed - standing
                standing += diff
                ans += diff
                # print needed, standing, count, ans
            standing += count

    return str(ans)

T = input()
for i in xrange(1, T+1):
    ans = 'Case #' + str(i) + ': ' + solve()
    print ans
    out.write(ans + '\n')
# No change after this

out.close()
