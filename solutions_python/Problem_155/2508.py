__author__ = 'mnach'
from engine import problem

converter = lambda x, i: int(x) if not i else [int(xi) for xi in x]


class Problem(problem.BaseProblem):
    # file_name = 'A-example.in'
    file_name = 'A-small-attempt0.in'
    # file_name = 'A-large-practice.in'
    case_kwargs = {'do_enumerate': True,
                   'data_converter': converter,
                   'lines_count': 1}

    def solve(self, data):
        s_max, elements = data
        if s_max + 1 != len(elements):
            raise ValueError('Not valid s_max {!r} line: {}'.format(data, self._reader._current_case))

        return self.brute_force_solve(s_max, elements)

    def brute_force_solve(self, s_max, elements):
        # calculate standing audience count if count doesn't enough add some friends
        standing_audience = 0
        invited_friends = 0
        for shyness_level, audience_count in enumerate(elements):
            if standing_audience < shyness_level:
                # invite more friends!
                invited_friends += shyness_level - standing_audience
                standing_audience = shyness_level
            standing_audience += audience_count
        return invited_friends

Problem().run()