def solve():
    Smax, profile = raw_input().split()
    Smax = int(Smax)
    invite_more = 0
    num_standup = 0
    for i in range(0, Smax+1):
        num_people = int(profile[i])
        if num_people == 0:
            continue
        else:
            if num_standup < i:
                need = i - num_standup
                invite_more += need
                num_standup += need
            if num_standup >= i:
                num_standup += num_people
                continue
            else:
                print 'hey this should not happen'
    return invite_more


T = int(raw_input())
for i in range(T):
    print 'Case #%d: %s' % (i+1, solve())
