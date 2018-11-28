import sys

def best(i, n):
    result = 0
    left = (1 << n) - i - 1
    for i in range(n):
        if(left > 0):
            result |= 1 << (n - i - 1)
        else:
            return (1 << n) - result
        left -= 1
        left >>= 1
    return (1 << n) - result

def worst(i, n):
    result = 0
    left = i
    for i in range(n):
        if(left > 0):
            result |= 1 << (n - i - 1)
        else:
            return result + 1
        left -= 1
        left >>= 1
    return result + 1

if __name__=='__main__':
    n = int(sys.stdin.readline())
    for i in range(n):
        sys.stdout.write("Case #{}: ".format(i + 1))
        teams, prizes = tuple(map(int, sys.stdin.readline().split()))
        #print(teams)
        st = 0
        ed = 1 << teams
        while(st < ed - 1):
            #print(st, ed)
            mid = (st + ed) >> 1
            if best(mid, teams) <= prizes:
                st = mid
            else:
                ed = mid
        could = st
        while(prizes >= best(could + 1, teams) and could != (1 << teams) - 1):
            could += 1

        st = 0
        ed = 1 << teams
        while(st < ed - 1):
            mid = (st + ed) >> 1
            if worst(mid, teams) <= prizes:
                st = mid
            else:
                ed = mid - 1
        guaranteed = st
        while(prizes >= worst(guaranteed + 1, teams) and guaranteed != (1 << teams) - 1):
            guaranteed += 1

        sys.stdout.write("{} {}\n".format(guaranteed, could))
        #sys.stderr.write("{} {}\n".format(worst(guaranteed, teams), best(could, teams)))
        #sys.stderr.write("{} {}\n".format(prizes, prizes))
        #sys.stderr.write("{} {}\n".format(worst(guaranteed + 1, teams), best(could + 1, teams)))

