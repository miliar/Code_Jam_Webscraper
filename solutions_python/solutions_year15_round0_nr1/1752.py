# Created By: Bryce Besler

T = int(raw_input());
for t in xrange(T):
    line = str(raw_input()).split(' ');
    s_max = int(line[0]);
    people = line[1];

    peopleStanding = 0
    friendsToBring = 0
    for i in xrange(s_max+1):
        if peopleStanding < i:
            friendsToBring += i - peopleStanding
            peopleStanding += i - peopleStanding
        peopleStanding += int(people[i])

    print "Case #{t}: {ans}".format(t=t+1, ans=friendsToBring)

