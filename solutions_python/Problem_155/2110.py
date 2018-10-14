from sys import stdin

def needed_friends(max_shyness, audience):
    friends = 0
    standing_up = 0
    for needed_shyness, people in enumerate(audience):
        if people == 0:
            continue
        if needed_shyness <= standing_up:
            standing_up += people
        else:
            invite = needed_shyness - standing_up
            friends += invite
            standing_up += people + invite
    return friends

T = int(stdin.readline())
for t in range(1, T + 1):
    max_shyness_str, audience_str = stdin.readline().strip().split(' ')
    max_shyness = int(max_shyness_str)
    audience = [int(c) for c in audience_str]
    print 'Case #{}: {}'.format(t, needed_friends(max_shyness, audience))
