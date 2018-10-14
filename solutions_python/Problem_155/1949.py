class TestCase(object):

    def __init__(self, s_max, people):
        self.s_max = s_max
        self.people = people
        self.friends = 0

    def __repr__(self):
        return 'S: {smax}, People: {people}'.format(smax=self.s_max, people=self.people)

    def solve(self):

        standing_people = int(self.people[0])

        for i in range(1, len(self.people)):
            if i > standing_people + self.friends:
                self.friends += i - (standing_people + self.friends)
            standing_people += int(self.people[i])


def run():
    with open('input', 'r') as input:
        # Get the number of test cases
        test_cases_number = int(input.readline().replace('\n', ''))
        test_cases = []
        for i in range(test_cases_number):
            test_case_line = input.readline().replace('\n', '')
            split = test_case_line.split(' ')
            test_case = TestCase(int(split[0]), split[1])
            test_cases.append(test_case)

        for i, test_case in enumerate(test_cases):
            test_case.solve()
            print 'Case #{tc}: {friends}'.format(tc=i+1,friends=test_case.friends)


if __name__ == '__main__':
    run()
