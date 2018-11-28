def solve(s, k):
    count = 0
    s = list(s)
    for i in range(len(s)-k + 1):
        if s[i] == '-':
            count += 1
            for j in range(i, i+k):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'

    if '-' in s:
        return 'IMPOSSIBLE'
    else:
        return count

if __name__ == "__main__":
    t = int(raw_input())

    for caseNr in xrange(1, t+1):
        s = raw_input()
        s = s.split()
        print("Case #%i: %s" % (caseNr, solve(s[0], int(s[1]))))
