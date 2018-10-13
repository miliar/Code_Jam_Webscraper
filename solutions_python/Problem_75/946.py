# coding: utf-8

import unittest
import sys


def cast_spell(elements, combinations, opposites):
    spell = []
    for element in elements:
        if spell and (element + spell[-1]) in combinations:
            combined = combinations[element + spell[-1]]
            spell.pop()
            spell.append(combined)
        elif spell and (spell[-1] + element) in combinations:
            combined = combinations[spell[-1] + element]
            spell.pop()
            spell.append(combined)
        elif spell and find_opposites(spell, element, opposites):
            spell = []
        else:
            spell.append(element)
    return spell


def find_opposites(spell, element, opposites):
    for se in spell:
        if (se + element) in opposites:
            return True
        elif (element + se) in opposites:
            return True
    return False


class MagickaTest(unittest.TestCase):

    def test_cast_spell(self):
        elements = 'EA'
        combinations = {}
        opposites = set()
        self.assertEqual(cast_spell(elements, combinations, opposites),
                         ['E', 'A'])

        elements = 'RRQR'
        combinations = {'QR': 'I'}
        opposites = set()
        self.assertEqual(cast_spell(elements, combinations, opposites),
                         ['R', 'I', 'R'])

        elements = 'RRQR'
        combinations = {'RQ': 'I'}
        opposites = set()
        self.assertEqual(cast_spell(elements, combinations, opposites),
                         ['R', 'I', 'R'])

        elements = 'FAQFDFQ'
        combinations = {'QF': 'T'}
        opposites = set(['QF'])
        self.assertEqual(cast_spell(elements, combinations, opposites),
                         ['F', 'D', 'T'])

        elements = 'FAQFDFQ'
        combinations = {'FQ': 'T'}
        opposites = set(['FQ'])
        self.assertEqual(cast_spell(elements, combinations, opposites),
                         ['F', 'D', 'T'])

        elements = 'QEEEERA'
        combinations = {'EE': 'Z'}
        opposites = set(['QE'])
        self.assertEqual(cast_spell(elements, combinations, opposites),
                         ['Z', 'E', 'R', 'A'])

        elements = 'QW'
        combinations = {}
        opposites = set(['QW'])
        self.assertEqual(cast_spell(elements, combinations, opposites),
                         [])


def main():
    indata = open(sys.argv[1])
    outdata = open(sys.argv[2], 'w')
    t = int(indata.readline().strip())
    print t
    for i in range(t):
        combinations = {}
        opposites = set()
        line_args = indata.readline().strip().split(' ')
        c = int(line_args.pop(0).strip())
        for j in range(c):
            comb = line_args.pop(0)
            combinations[comb[0:2]] = comb[2]
        d = int(line_args.pop(0).strip())
        for j in range(d):
            oppo = line_args.pop(0)
            opposites.add(oppo)
        n = line_args.pop(0)
        elements = line_args.pop(0)
        print elements, combinations, opposites
        res = cast_spell(elements, combinations, opposites)
        res_str = str(res).replace("'", "")
        outdata.write("Case #%d: %s\n" % (i + 1, res_str,))

    indata.close()
    outdata.close()


if __name__ == '__main__':
    main()