from base import GoogleJamBaseClass
from collections import OrderedDict


class A(GoogleJamBaseClass):
    def read_case(self, input_file):
        return input_file.readline().rstrip('\n')

    def solve(self, case):
        config = OrderedDict([
            ('0', {
                'Z': 1,
                'E': 1,
                'R': 1,
                'O': 1,
            }),
            ('6', {
                'S': 1,
                'I': 1,
                'X': 1,
            }),
            ('2', {
                'T': 1,
                'W': 1,
                'O': 1,
            }),
            ('8', {
                'E': 1,
                'I': 1,
                'G': 1,
                'H': 1,
                'T': 1,
            }),
            ('7', {
                'S': 1,
                'E': 2,
                'V': 1,
                'N': 1,
            }),
            ('5', {
                'F': 1,
                'I': 1,
                'V': 1,
                'E': 1,
            }),
            ('4', {
                'F': 1,
                'O': 1,
                'U': 1,
                'R': 1,
            }),
            ('9', {
                'N': 2,
                'I': 1,
                'E': 1,
            }),
            ('1', {
                'O': 1,
                'N': 1,
                'E': 1,
            }),
            ('3', {
                'T': 1,
                'H': 1,
                'R': 1,
                'E': 2,
            })
        ])
        letter_stats = {}
        result = {}
        for idx, letter in enumerate(case):
            if letter not in letter_stats:
                letter_stats[letter] = 0
            letter_stats[letter] += 1
        for number, letters in config.iteritems():
            minimum = len(case)
            for letter, count in letters.iteritems():
                if letter not in letter_stats:
                    minimum = 0
                else:
                    minimum = min(letter_stats[letter] / count, minimum)
            if minimum > 0:
                for letter, count in letters.iteritems():
                    letter_stats[letter] -= minimum * count
                result[number] = minimum
        sorted_result = OrderedDict(sorted(result.items()))
        phone = ''
        for number, count in sorted_result.iteritems():
            phone += number * count
        return phone

A().run('A-large.in')