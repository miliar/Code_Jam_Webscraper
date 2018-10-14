import sys

n_tests = int(sys.stdin.readline())
for i in range(n_tests):
    n_people, people = sys.stdin.readline().split()
    n_people = int(n_people);
    people = [int(x) for x in list(people)]
    n_people_ovation, n_people_needed = 0, 0
    for n_needed, person in enumerate(people):
        if n_people_ovation < n_needed:
            n_people_needed += n_needed-n_people_ovation
            n_people_ovation = n_needed
        n_people_ovation += person
    print("Case #%d: %d" % (i+1, n_people_needed, ))
