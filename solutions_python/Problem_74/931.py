import sys


class Runner(object):
    def __init__(self, test_case):
        self.test_case = test_case
        self.state = {
            "O": 1,
            "B": 1,
        }
    def run(self):
        def done():
            return not bool(self.test_case.instructions)
        def next(robot):
            next_buttons = [i['button'] for i in self.test_case.instructions if i['robot'] == robot]
            return next_buttons[0] if next_buttons else 0
        def next_button():
            return self.test_case.instructions[0]
        def press():
            self.test_case.instructions.pop(0)
        def wait():
            pass
        def move(robot, forward=True):
            if forward:
                self.state[robot] += 1
            else:
                self.state[robot] -= 1

        steps = 0
        while True:
            if done(): break
            n = next_button()
            for robot in self.state.keys():
                robots_next = next(robot)
                if robots_next == self.state[robot]:
                    if n['robot'] == robot:
                        press()
                    else:
                        wait()
                else:
                    move(robot, self.state[robot] < robots_next)
            steps += 1

        print 'Case #%d: %d' % (self.test_case.number, steps)

class TestCase(object):
    def __init__(self, spec_string, number):
        self.number = number
        self.instructions = []
        spec = spec_string.strip().split(" ")
        spec.pop(0) # discard count.
        while spec:
            robot = spec.pop(0)
            button = int(spec.pop(0))
            t = {'robot': robot, 'button': button}
            self.instructions.append(t)

def read_input():
    lines = sys.stdin.readlines()
    return [TestCase(test_case_spec, test_case_number) for test_case_spec, test_case_number in zip(lines[1:], xrange(1, len(lines))) ]

if __name__ == '__main__':
    test_cases = read_input()
    for test_case in test_cases:
        Runner(test_case).run()
