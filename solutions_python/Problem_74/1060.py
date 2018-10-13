#!/usr/bin/env python
#
# Author    : Mahendra Chintomby (mchintomby@gmail.com)
#
"""
"""
import fileinput
import cStringIO


def bot_trust(infile=None):
    if infile is None:
        infile = fileinput.input()

    def get_lines(n):
        lines = list()
        for i in xrange(n):
            lines.append(infile.readline())
        return lines

    def get_seconds(line):
        inputs = line.split()
        inputs.pop(0)
        tick = 0
        robot_positions = {
            'O': 1,
            'B': 1,
        }

        button_map = dict()
        button_map['O'] = list()
        button_map['B'] = list()
        first = inputs[0]
        button_seq = list()
        while inputs:
            r = inputs.pop(0)
            p = int(inputs.pop(0))
            button_map[r].append(p)
            button_seq.append((r,p))

        def is_done():
            return not bool(button_map['O'] or button_map['B'])

        def can_push(pushed, robot, position):
            if not pushed and robot != first:
                # can't push button yet
                return False
            button_list = button_map[robot]
            return bool(button_list) and (button_list[0] == position)

        def next_pos(pushed, robot, position):
            button_list = button_map[robot]
            if not button_list:
                return position
            if button_list[0] == position:
                return position
            elif button_list[0] < position:
                return position - 1
            else:
                return position + 1

        robots = button_map.keys()
        ever_pushed = False
        while not is_done():
            tick += 1
            next_robot, next_position = button_seq[0]
            pushed = False
            for robot in robots:
                if can_push(ever_pushed, robot, robot_positions[robot]):
                    if not pushed:
                        # only one button can be pushed in a tick
                        if next_robot == robot and next_position == robot_positions[robot]:
                            # make sure it's the next button
                            pushed = True
                            button_map[robot].pop(0)
                            button_seq.pop(0)
                else:
                    robot_positions[robot] = next_pos(ever_pushed, robot, robot_positions[robot])
                ever_pushed = ever_pushed or pushed
        return tick

    case = 1
    case_results = list()
    while True:
        line = infile.readline()
        if not line:
            break
        try:
            cases = int(line)
        except ValueError:
            print 'Test case count not found'
            break
        for line in get_lines(cases):
            case_results.append('Case #%d: %s' % (case, get_seconds(line)))
            case += 1
    return case_results

def test():
    expected = [
        'Case #1: 6',
        'Case #2: 100',
        'Case #3: 4',
        'Case #4: 11',
    ]

    result = bot_trust(cStringIO.StringIO(
    '4\n'
    '4 O 2 B 1 B 2 O 4\n'
    '3 O 5 O 8 B 100\n'
    '2 B 2 B 1\n'
    '3 B 5 B 1 O 1\n'))

    assert expected == result, result

    print '\n'.join(result)

if __name__ == "__main__":
    print '\n'.join(bot_trust())

