from sortedcontainers import SortedDict

class Bathroom(object):

    vacancies = SortedDict()

    def __init__(self, n):
        self.vacancies.clear()
        self.vacancies[n] = 1

    def add_person(self):
        vacancy = self.vacancies.peekitem()
        if vacancy[1] == 1:
            self.vacancies.popitem()
        else:
            self.vacancies[vacancy[0]] = vacancy[1] - 1
        right_dist = (vacancy[0] - 1) // 2
        left_dist = vacancy[0] - 1 - right_dist
        if left_dist > 0:
            if self.vacancies.has_key(left_dist):
                self.vacancies[left_dist] = self.vacancies[left_dist] + 1
            else:
                self.vacancies[left_dist] = 1
        if right_dist > 0:
            if self.vacancies.has_key(right_dist):
                self.vacancies[right_dist] = self.vacancies[right_dist] + 1
            else:
                self.vacancies[right_dist] = 1
        return left_dist, right_dist

if __name__ == '__main__':
    with open('C-small-1-attempt2.in', 'r') as file:
        line_no = 0
        for line in file:
            if line_no == 0:
                line_no += 1
                continue
            words = line.split()
            n = long(words[0])
            k = long(words[1])
            bathroom = Bathroom(n)
            i = 0
            while i < k - 1:
                bathroom.add_person()
                i += 1
            last_dists = bathroom.add_person()
            print('Case #' + str(line_no) + ': ' + str(last_dists[0]) + ' ' + str(last_dists[1]))
            line_no += 1
            
