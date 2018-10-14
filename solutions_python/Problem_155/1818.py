cases = int(raw_input())

case = 1
while cases > 0:
    info = raw_input().split(" ")
    max_shyness = int(info[0])
    shyness_levels = info[1]

    invited_friends = 0
    current_standing = 0
    for level, people in enumerate(shyness_levels):
        people = int(people)
        # weve got enough people lets increment the standers
        if current_standing+invited_friends >= level:
            current_standing += people
        # Not enough lets invite some friends
        else:
            invited_friends += level - (current_standing + invited_friends)
            current_standing += people

    print "Case #{0}: {1}".format(case, invited_friends)


    case+=1
    cases-=1
