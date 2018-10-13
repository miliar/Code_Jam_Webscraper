def solve(s):
    if len(s) == 1:
        return s[0]
    l = 0
    r = 0
    s = list(s)
    for i in range(len(s)-1):

        if s[i]>s[i+1]:
            break
        elif s[i]< s[i+1]:
            r +=1
            l += 1
        else:
            r += 1

    if list(s) == sorted(s):
        return ''.join(s)
    else:
        if l == 0 and s[0] == '1':
            return '9'*(len(s)-1)
        else:
            for i in range(l, len(s)):
                if i == l:
                    s[i]  = str(int(s[i]) - 1)
                else:
                    s[i] = '9'
            return ''.join(s)


if __name__ == "__main__":
    t = int(raw_input())

    for caseNr in xrange(1, t+1):
        s = raw_input()
        print("Case #%i: %s" % (caseNr, solve(s)))
