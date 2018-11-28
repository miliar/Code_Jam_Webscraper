def solve(s):
    s = ['0'] + s
    for i in range(len(s)-1,0,-1):
        if int(s[i]) < int(s[i-1]):
            for j in range(i,len(s)):
                if s[j] == '9': break
                s[j] = '9'
            s[i-1] = '%d' % (int(s[i-1])-1)

    return int(''.join(s))


_T = int(input())

for _i in range(1, _T + 1):

    s = list(input())

    print("Case #%d: %d" % (_i, solve(s)))
