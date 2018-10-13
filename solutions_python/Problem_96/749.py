#
#26 surprising max=10
#
#26 not surprising max = 9
#
#28 surprising max = 10
#
#28 not surprising max = 10
#
#27 surprising max = 10
#
#27 not surprising max = 9 

inf = open('/home/nullard/Downloads/B-small-attempt0.in')

#inf = open('../data/problemb.in')
num_cases = int(inf.readline().strip())

print num_cases
for i in range(1, num_cases + 1):
    header = 'Case #' + str(i) + ': '
    nextline = inf.readline().split()
    googlers = int(nextline[0])
    surprises = int(nextline[1])
    passing = int(nextline[2])
    totals = map(int, nextline[3:])
    successes = 0
    if passing > 10:
        print header + str(successes)
        continue
    for score in totals:
        if score < 2 and passing > 0:
            continue
        elif (score + 2) / 3 >= passing:
            successes += 1
            continue
        elif surprises > 0 and (score + 4) / 3 >= passing:
            successes += 1
            surprises -= 1
            continue
    print header + str(successes)