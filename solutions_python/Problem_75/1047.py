#!/usr/bin/env python
#
# Author    : Mahendra Chintomby (mchintomby@gmail.com)
#
"""
"""
import fileinput
import cStringIO


def magicka(infile=None):
    if infile is None:
        infile = fileinput.input()

    def get_lines(n):
        lines = list()
        for i in xrange(n):
            lines.append(infile.readline())
        return lines

    def foo(line):
        inputs = line.split()

        n = int(inputs.pop(0))
        formed_elements = inputs[0:n]
        formed_elements = dict((frozenset((s[0],s[1])),s[2]) 
                for s in formed_elements)
        inputs = inputs[n:]
        def check_formed(elements):
            if len(elements) < 2:
                return elements
            e = formed_elements.get(frozenset(elements[-2:]))
            if e:
                elements.pop()
                elements.pop()
                elements.append(e)
            return elements

        n = int(inputs.pop(0))
        opposed_elements = inputs[0:n]
        opposed_elements = dict([(s[0],s[1]) for s in opposed_elements] + [
                    (s[1], s[0]) for s in opposed_elements])
        inputs = inputs[n:]
        def check_opposed(elements):
            if not elements:
                return elements

            opposed = opposed_elements.get(elements[-1])
            if opposed and opposed in elements:
                return list()
            return elements

        int(inputs.pop(0))
        invoked_elements = list(inputs[0])

        result = list()
        for e in invoked_elements:
            result.append(e)
            result = check_opposed(check_formed(result))

        return '[%s]' % ', '.join(result)

    case = 1
    case_results = list()
    while True:
        line = infile.readline()
        if not line:
            break
        try:
            cases = int(line)
        except ValueError:
            print 'Test case count not found'
            break
        for line in get_lines(cases):
            case_results.append('Case #%d: %s' % (case, foo(line)))
            case += 1

    return case_results

def test():
    expected = [
        'Case #1: [E, A]',
        'Case #2: [R, I, R]',
        'Case #3: [F, D, T]',
        'Case #4: [Z, E, R, A]',
        'Case #5: []',
    ]

    result = magicka(cStringIO.StringIO(
        '5\n'
        '0 0 2 EA\n'
        '1 QRI 0 4 RRQR\n'
        '1 QFT 1 QF 7 FAQFDFQ\n'
        '1 EEZ 1 QE 7 QEEEERA\n'
        '0 1 QW 2 QW\n'
    ))

    print '\n'.join(result)

    assert expected == result, expected


if __name__ == "__main__":
    print '\n'.join(magicka())

