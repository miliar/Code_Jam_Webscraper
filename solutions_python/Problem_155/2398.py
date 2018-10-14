__author__ = 'Samir Malpande'

lines = [line.rstrip('\n') for line in open('A-large.in')]

total_cases, cases = lines[0], lines[1:]
f = open('A-output-large.out', 'w')

for i, case in enumerate(cases):
    persons_standing = 0
    friend = 0
    l = [x.strip() for x in case.split(' ')]
    max_shyness, Si = l[0], l[1]

    for index, person in enumerate(Si):
        print(person)
        if int(person) != 0:
            if persons_standing + friend >= index:
                persons_standing += int(person)
            else:
                friend += index - (persons_standing + friend)
                persons_standing += int(person)

    output = "Case #{}: {}".format(i + 1, friend)
    f.write(output + "\n")

f.close()