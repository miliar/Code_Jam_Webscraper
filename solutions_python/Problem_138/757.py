def get_win(x, y, n):
    j = 0
    cnt = 0
    for i in x:
        while j < n and y[j] < i:
            j += 1
        if j == n:
            break
        cnt += 1
        j += 1
    return cnt


def main():
    filename = raw_input()
    fp = open(filename + '.in', 'r')
    wfp = open(filename + '.out', 'w')
    for it in range(int(fp.readline())):
        n = int(fp.readline())
        Naomi = sorted(map(lambda x: float(x), fp.readline().split(' ')))
        Ken = sorted(map(lambda x: float(x), fp.readline().split(' ')))
        dp = get_win(Ken, Naomi, n)
        p = n - get_win(Naomi, Ken, n)
        #print Naomi
        #print Ken
        output = 'Case #%d: %d %d\n' % (it+1, dp, p)
        #print output
        wfp.write(output)

main()