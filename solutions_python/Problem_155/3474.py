import sys

tc = int(raw_input())
for t in range(1, tc + 1):
    s_max, digits = sys.stdin.readline().strip().split()
    print 'Case #%d:' % (t),
    audience = 0
    friends = 0
    for i in xrange(int(s_max) + 1):
        if int(digits[i]) > 0:
            if i <= audience:
                audience += int(digits[i])
            else:
                friends += i - audience
                audience += friends + int(digits[i])
        #print audience,
    print friends
