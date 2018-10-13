def extra_friends(s):
    ans = 0
    standing = int(s[0])
    for i in range(1, len(s)):
        if standing < i:
            ans += (i - standing)
            standing = i + int(s[i])
        else:
            standing += int(s[i])

    return ans

T = int(raw_input())

for i in range(T):
    n, s = raw_input().split(" ")
    print "Case #%i: %i" % (i + 1, extra_friends(s))
