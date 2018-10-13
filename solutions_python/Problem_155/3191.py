

#with open('sample.in') as f:
with open('A-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        data = f.readline()
        max_shy, people = data.split(' ')
        people = list(people.strip())

        more_friends = 0
        people_standing = int(people[0])

        for i, p in enumerate(people[1:]):
            if (i+1) > people_standing:
                extras = (i+1) - people_standing
                more_friends += extras
                people_standing += extras

            people_standing += int(p)

        print('Case #%s: %s' % (str(puzzle_count + 1), more_friends))
