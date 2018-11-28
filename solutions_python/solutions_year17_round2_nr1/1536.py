import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '.'))
from core import *

# -----------------------------------------------------------------------------
# Round 1B 2017
# Problem A. Steed 2: Cruise Control
# -----------------------------------------------------------------------------
class CruiseControl(Solution):
    enabled = True

    def handle(self, case):
        inputs = case.case_input.split(' ')
        max_distance = float(inputs[0])
        n_horses = int(inputs[1])

        horse_data = {}
        horse_init_distance = []
        index = 2
        for n_horse in xrange(n_horses):
            horse_data[n_horse] = {}
            horse_data[n_horse]['id'] = n_horse
            horse_data[n_horse]['init'] = float(inputs[index + n_horse])
            index += 1
            horse_data[n_horse]['speed'] = float(inputs[index + n_horse])

        max_time_to_reach_end = 0
        for data in horse_data.values():
            time_to_reach_end = (max_distance - data['init']) / data['speed']
            max_time_to_reach_end = max(max_time_to_reach_end, time_to_reach_end)
        max_speed = max_distance / max_time_to_reach_end

        case.register_case_output(max_speed)

    def case_samples(self):
        return [
            '2525 1 2400 5',
            '300 2 120 60 60 90',
            '100 2 80 100 70 10',
        ]

    def case_files(self):
        return [
            '../data/2017-google-code-jam/round-1b/B-small-attempt0.in',
            '../data/2017-google-code-jam/round-1b/B-large.in',
        ]

# -----------------------------------------------------------------------------
# Round 1B 2017
# Problem B. Steed 2: Cruise Control
# -----------------------------------------------------------------------------
class CruiseControl(Solution):
    enabled = True

    def handle(self, case):
        inputs = case.case_input.split(' ')
        print inputs
        max_distance = float(inputs[0])
        n_horses = int(inputs[1])

        horse_data = {}
        horse_init_distance = []
        index = 2
        for n_horse in xrange(n_horses):
            horse_data[n_horse] = {}
            horse_data[n_horse]['id'] = n_horse
            horse_data[n_horse]['init'] = float(inputs[index + n_horse])
            index += 1
            horse_data[n_horse]['speed'] = float(inputs[index + n_horse])

        max_time_to_reach_end = 0
        for data in horse_data.values():
            time_to_reach_end = (max_distance - data['init']) / data['speed']
            max_time_to_reach_end = max(max_time_to_reach_end, time_to_reach_end)
        max_speed = max_distance / max_time_to_reach_end

        case.register_case_output(max_speed)

    def run(self, *args, **kwargs):
        print 'Running code-based test cases'
        with timed_context('Run code-based test cases'):
            for case_number, case_input in enumerate(self.case_samples()):
                with timed_context('Code test case #%s' % case_number):
                    case = Case(case_number, case_input.strip())
                    self.handle(case)
                    print case.solution()
        for filename in self.case_files():
            print 'Running file-based test cases in [%s]' % filename
            with timed_context('Run file-based test cases in [%s]' % filename):
                for case in self.custom_case_iterator(filename):
                    with timed_context('File %s test case #%s' % (filename, case.case_number)):
                        self.handle(case)

    def custom_case_iterator(self, filename):
        with open(filename, 'r') as source, open(filename + '.out', 'w') as destination:
            case_number = 0
            next(source)
            for case_input in source:
                case_number += 1
                adjusted_case_input = case_input.strip()
                n_next_inputs = int(adjusted_case_input.split(' ')[1])
                for _ in xrange(n_next_inputs):
                    adjusted_case_input += ' ' + next(source).strip()
                case = Case(case_number, adjusted_case_input.strip())
                yield case
                destination.write(case.solution())

    def case_samples(self):
        return [
            '2525 1 2400 5',
            '300 2 120 60 60 90',
            '100 2 80 100 70 10',
        ]

    def case_files(self):
        return [
            '../data/2017-google-code-jam/round-1b/A-small-attempt0.in',
            '../data/2017-google-code-jam/round-1b/A-large.in',
        ]


run(__name__)
