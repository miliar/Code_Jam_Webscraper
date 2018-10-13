#!/opt/local/bin/python

import sys
from itertools import count

def get_next_position(position_it, robot):
    while True:
        try:
            next = position_it.next()
        except StopIteration:
            return None
        if next[1] == robot:
            return next[0]

input_it = iter(sys.stdin.readlines())

T = int(input_it.next())

for case in range(T):
    _sequence = input_it.next().split()
    sequence = zip([int(i) for i in _sequence[2::2]], _sequence[1::2])

    position = {'O': 1, 'B': 1}
    robot_it = {'O': iter(sequence), 'B': iter(sequence)}

    next_position = {'O': get_next_position(robot_it['O'], 'O'), 'B': get_next_position(robot_it['B'], 'B')}

    action_it = iter(sequence)
    try:
        action = action_it.next()
        acted = False

        for i in count(1):
            # print 'status: (%3d, %3d)' % (position['O'], position['B'])
            for robot in 'O', 'B':
                if not next_position[robot] == None:
                    if action[0] == position[robot] and action[1] == robot:
                        acted = True
                        # print 'robot %s pushed button %s in round %s' % (robot, position[robot], i)
                    elif position[robot] < next_position[robot]:
                        position[robot] += 1
                    elif position[robot] > next_position[robot]:
                        position[robot] -= 1
            if acted:
                next_position[action[1]] = get_next_position(robot_it[action[1]], action[1])
                action = action_it.next()
                acted = False

    except StopIteration:
        print 'Case #%s: %s' % (case + 1, i)

