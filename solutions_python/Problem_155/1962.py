def solve(smax, aud_count):
    friends_needed = 0
    curr_aud_count = 0
    for i in xrange(smax+1):
        if curr_aud_count < i:
            friends_needed += i-curr_aud_count
            curr_aud_count += i-curr_aud_count
        curr_aud_count += int(aud_count[i])
    return friends_needed


f = open('A-large.in', 'r')
test_count = int(f.readline())
for i in xrange(test_count):
    smax, aud_count = f.readline().split()
    ret = solve(int(smax), aud_count)
    print "Case #%d: %d" % (i+1, ret)
f.close()