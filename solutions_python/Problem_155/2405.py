__author__ = 'ramon'


from multiprocessing import Pool


def parse(problem):
    friends_required = 0
    audience_standing_up = 0
    audience_requirement = 0
    for a in problem:
        value = int(a)
        if audience_requirement > audience_standing_up:
            difference = audience_requirement - audience_standing_up
            friends_required += difference
            audience_standing_up += difference
        audience_standing_up += value
        audience_requirement += 1
    return friends_required


class ParseFriends(object):

    def __init__(self, list_of_cases):
        self._list_of_cases = list_of_cases
        self._pool = Pool(4)

    def result(self):
        res = self._pool.map(parse, self._list_of_cases)
        for a in xrange(len(res)):
            print 'Case #{}: '.format(a+1), res[a]


def main():
    num_test_cases = input()
    list_to_process = list()
    for a in xrange(num_test_cases):
        s = raw_input()
        s = s.split()
        list_to_process.append(s[1])
    parser = ParseFriends(list_to_process)
    parser.result()


main()