import sys
import itertools as it

class Solver(object):

    def __init__(self, iterable, L, D, N):
        self.L, self.D, self.N = L, D, N

        self._parse_dict(iterable)
        self._parse_test_cases(iterable)

    def solve(self):
        for i, num_choices in enumerate(self._num_choices[:]):
            if num_choices == -1:
                choices = self._choices_at_positions[i]
                letter_index = 1
                subwords = choices[0]
                while letter_index < self.L:
                    subwords_iter = it.product(subwords, choices[letter_index])
                    subwords = []
                    for subword in subwords_iter:
                        subword = ''.join(subword)
                        if subword in self._possible_subwords[letter_index]:
                            subwords.append(subword)
                    letter_index += 1
                self._num_choices[i] = len(subwords)
        return self._num_choices

    def _parse_dict(self, word_list):
        # we save the possible subwords, i.e. 1 char combinations, 2 chars
        # combinations, ... . 1st set won't be used but will make indexing more
        # natural later
        self._possible_subwords = [set() for i in range(self.L)]

        # at each index in the word, save all the possible chars. Used to
        # get rid of impossible letters in a choice set, e.g. (zab) when no
        # word in the dictionary ever had a z in 1st position
        self._letters_at_position = [set() for i in range(self.L)]

        for i in range(self.D):
            word = word_list.next().strip()
            for j, letter in enumerate(word):
                self._letters_at_position[j].add(letter)

                self._possible_subwords[j].add(word[:j+1])

    def _parse_test_cases(self, case_list):
        self._choices_at_positions = [[] for i in range(self.N)]
        self._num_choices = []
        for case_index in range(self.N):
            case = case_list.next().strip()

            if '(' not in case:
                if case in self._possible_subwords[-1]:
                    self._num_choices.append(1)
                else:
                    self._num_choices.append(0)
                continue

            for index in range(self.L):

                # sure of the letter
                if case[0] != '(':
                    choices = [case[0]]
                    consumed = 1
                # not sure of the letter
                else:
                    end_index = case.index(')')
                    choices = self._get_real_choices(case[1:end_index], index)
                    consumed = end_index + 1

                if choices:
                    self._choices_at_positions[case_index].append(choices)
                    case = case[consumed:]
                else:
                    # no possible choice at that char index. No need to keep
                    # reading the word
                    self._num_choices.append(0)
                    break # next test case
            else:
                self._num_choices.append(-1)

    def _get_real_choices(self, letters, index):
        choices = []
        for letter in letters:
            if letter in self._letters_at_position[index]:
                choices.append(letter)
        return choices

def main(args):
    f = open(args[0])
    try:
        L, D, N = f.readline().split()
        solver = Solver(f, int(L), int(D), int(N))
    finally:
        f.close()

    response = solver.solve()

    responses = []
    for i, test_case in enumerate(response):
        responses.append("Case #%d: %d\n" % (i + 1, test_case))

    f = open(args[0][:-2] + "out", 'w')
    f.writelines(responses)
    f.close()

if __name__ == "__main__":
    sys.argv.pop(0)
    main(sys.argv)
