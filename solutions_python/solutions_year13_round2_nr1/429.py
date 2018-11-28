import sys

def solve(me, motes):
    if len(motes) == 0:
        return 0
    else:
        if motes[0] < me:
            return solve(me + motes[0], motes[1:])
        else:
            if me == 1:
                return len(motes)
            ret = 1 + solve(me + me - 1, motes)
            if ret < len(motes):
                return ret
            else:
                return len(motes)

cases = int(sys.stdin.readline())
for case in range(cases):
    case = case + 1
    l1 = sys.stdin.readline()
    l2 = sys.stdin.readline()
    me,_ = l1.split()
    me = int(me)
    motes = map(int, l2.split())
    motes.sort()
    print "Case #" + str(case) + ": " + str(solve(me, motes))

