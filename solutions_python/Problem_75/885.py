from collections import defaultdict

def solve(line):
    line = line.split()
    C = int(line[0])
    D = int(line[C+1])
    
    combines = dict((x[0] + x[1], x[2]) for x in line[1:C+1])
    combines.update((x[1] + x[0], x[2]) for x in line[1:C+1])

    opposes = defaultdict(list)
    for x in line[C+2:C+D+2]:
        opposes[x[0]].append(x[1])
        opposes[x[1]].append(x[0])

    elements = line[C+D+3]

    output = []
    counts = defaultdict(int)

    def opposes_something(x):
        for c in opposes[x]:
            if counts[c]:
                return True
        return False

    for el in elements:
        output.append(el)
        counts[el] += 1
        while len(output) >= 2:
            x = output[-2] + output[-1]
            if x in combines:
                counts[output[-1]] -= 1
                counts[output[-2]] -= 1
                output.pop()
                output.pop()
                counts[combines[x]] += 1
                output.append(combines[x])
            else:
                break

        if output:
            for c in opposes[output[-1]]:
                if counts[c]:
                    output = []
                    counts = defaultdict(int)
                    break

    return '[%s]' % ', '.join(output)

T = int(raw_input())
for t in range(1, T+1):
    print "Case #%d: %s" % (t, solve(raw_input()))
