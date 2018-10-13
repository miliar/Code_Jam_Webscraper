def run(moves, n):
    starts = sorted(moves, key=lambda x: x[0])
    ends = sorted(moves, key=lambda x: x[1])
    normal = sum([calcPrice(x[0], x[1], x[2], n) for x in moves])
    starts.append((ends[-1][1]+1, -1, 0))
    startUpto = endUpto = 0
    people = {}
    cost = 0
    while endUpto < len(moves):
        if starts[startUpto][0] <= ends[endUpto][1]:
            frm, to, num = starts[startUpto]
            people[frm] = people.get(frm, 0) + num
            startUpto += 1
        else:
            delete = ends[endUpto][2]
            while delete > 0:
                result = max(people)
                cost += calcPrice(result, ends[endUpto][1],
                        min(people[result], delete), n)
                if people[result] > delete:
                    people[result] -= delete
                    break
                else:
                    delete -= people[result]
                    del people[result]

            endUpto += 1

    return normal - cost

def calcPrice(start, stop, people, n):
    #print "%d people going from %d to %d" % (people, start, stop)
    d = stop - start
    return (d * n - ((d**2 - d) / 2)) * people

text = open("small.in", "rU").readlines()[1:]
cases = [(0, 0, [])]

for line in text:
    line = tuple(map(int, line.split()))
    if len(cases[-1][2]) == cases[-1][1]:
        cases.append((line[0], line[1], []))
    else:
        cases[-1][2].append(line)

cases = cases[1:]

for i, (n, m, moves) in enumerate(cases):
    print "Case #%d: %d" % (i+1, run(moves, n))
