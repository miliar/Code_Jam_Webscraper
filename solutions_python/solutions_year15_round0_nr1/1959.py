def find_friend_count(a, l):
    c = 0
    max_d = 0
    for i in xrange(l+1):
        j = ord(a[i]) - ord('0')
        if i - c > max_d:
            max_d = i - c
        c += j
    return max_d

t = int(raw_input())

for i in xrange(t):
    l, a = raw_input().strip().split()
    l = int(l)
    print "Case #" + str(i+1) + ":", find_friend_count(a, l)
