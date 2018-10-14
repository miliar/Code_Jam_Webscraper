cases = int(input())
for a in range(cases):
    caseno = a + 1
    caseq = input()
    maxshy, people = caseq.split()
    maxshy = int(maxshy)
    needed = 0
    reserve = 0
    for person in range(int(maxshy)):
        if people[person] == '0':
            if reserve == 0:
                needed += 1
            else:
                reserve-=1
        else:
          reserve += (int(people[person])-1)
    print("Case #%s: %s" % (str(caseno), str(needed)))
