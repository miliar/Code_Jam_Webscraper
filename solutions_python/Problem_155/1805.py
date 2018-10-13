
def get_min_members(smax, audience):
    standing = 0
    friends = 0
    i = 1
    standing += audience[0]
    while i <= smax:
        if standing < i:
            new_friends = i - standing
            standing += new_friends
            friends += new_friends
        standing += audience[i]
        i += 1
    return friends

# cases = [(4, "11111"), (1, "09"), (5, "110011"), (0, "1")]
t = input()
for i in range(t):
    smax, audience = raw_input().split()
    result = get_min_members(int(smax), map(int, audience))
    print "Case #%d: %d" % (i+1, result)
