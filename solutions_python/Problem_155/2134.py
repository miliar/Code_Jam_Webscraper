def calculate_friends(s_max, s):
    standing = 0
    added = 0
    for i,s_i in enumerate(s):
        s_i = int(s_i)
        if standing < i and i != 0:
            # Dont have sufficient standers, must add some
            people_needed = i - standing
            added += people_needed
            standing += people_needed
        standing += s_i
        #print i,s_i,added,standing
    return added

t = int(input())

for i in xrange(t):
    raw = raw_input().strip().split()
    s_max = raw[0]
    s = raw[1]
    friends_added = calculate_friends(s_max, s)
    print 'Case #' +  str(i+1) +': ' + str(friends_added)
