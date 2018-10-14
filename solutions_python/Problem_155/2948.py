class OvationSolver(object):
    """ Solves problem A of Qualification Round GCD'15 """

    def __init__(self, input_):
        self.max_shiness, self.shiness_info = input_.split()
        self.max_shiness = int(self.max_shiness)

    def solve(self):
        result, people_in_the_hall = 0, 0
        for indx, cnt in enumerate(self.shiness_info):
            cnt = int(cnt)
            additional = 0
            if cnt > 0 and people_in_the_hall < indx:
                additional = indx - people_in_the_hall
            people_in_the_hall += cnt + additional
            result += additional

        return result

if __name__ == '__main__':
    test_cases = int(raw_input())
    for test_case in xrange(1, test_cases + 1):
        print('Case #%s: %s' % (test_case, OvationSolver(raw_input()).solve()))
