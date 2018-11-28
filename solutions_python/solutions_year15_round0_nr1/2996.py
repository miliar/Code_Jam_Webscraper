cases = int(raw_input())

for i in range(1, cases+1):
    max_shyness, digits = [j for j in raw_input().split()]
    max_shyness = int(max_shyness)

    friends = 0
    standingPeople = 0

    for j in range(max_shyness+1):
        toStand = int(digits[j])
        neededStanding = j

        if toStand > 0:
            if standingPeople < neededStanding:
                neeeded = neededStanding - standingPeople

                friends += neeeded
                standingPeople += neeeded

        standingPeople += toStand

    print 'Case #%d: %d' % (i, friends)
