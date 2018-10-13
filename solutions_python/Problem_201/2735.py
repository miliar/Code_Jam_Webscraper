from collections import namedtuple

with open('C-small-1-attempt0.in', 'r') as f:
    lines = f.readlines()

t = lines[0]
examples = lines[1:]
nums = [num.strip().split(" ") for num in examples]

StallsToPersons = namedtuple('StallsToPersons', 'stalls, persons')
inputs = []
for n in nums:
    inputs.append(StallsToPersons(int(n[0]), int(n[1])))


def calculateSolution(input):
    stalls_num = input.stalls
    stalls = [False for i in xrange(stalls_num + 2)]
    stalls[0] = True
    stalls[-1] = True

    for p in xrange(0, input.persons):
        potential_stalls = {}
        last_occupied_left_stall = 0

        for i in xrange(0, len(stalls)):
            if stalls[i]:
                last_occupied_left_stall = i
            else:
                potential_stalls[i] = {'ls': i - last_occupied_left_stall - 1}

        last_occupied_right_stall = len(stalls) - 1
        for i in reversed(xrange(len(stalls))):
            if stalls[i]:
                last_occupied_right_stall = i
            else:
                potential_stalls[i]['rs'] = last_occupied_right_stall - i - 1

        max_closest_neighbor = -1
        stall = None
        items = [{'i': k, 'rs': v['rs'], 'ls': v['ls'],
                  'mins': min(v['ls'], v['rs']), 'maxs': max(v['ls'], v['rs'])}
                 for k, v in potential_stalls.iteritems()]
        items.sort(key=lambda x: (-x['mins'], -x['maxs']))

        # print 'Choose ', items[0]['i']
        stalls[items[0]['i']] = True
        last_item = items[0]
    return last_item

index = 1
for i in inputs:
    solution = calculateSolution(i)
    print 'Case #{}: {} {}'.format(index, solution['maxs'], solution['mins'])
    index += 1
