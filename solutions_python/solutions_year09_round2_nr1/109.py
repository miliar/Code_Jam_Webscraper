#!/usr/bin/python
# Python 2.6

import sys
from decimal import Decimal
from util import FileReader

def splitsubs(s):
    index = s.index('(') + 1
    count = 1
    while count > 0:
        if s[index] == '(':
            count += 1
        elif s[index] == ')':
            count -= 1
        index += 1

    return s[:index], s[index:]


class DTree:

    def __init__(self, input):
        input = input.strip()[1:-1].strip()
        splits = input.split(' ')
        self.value = Decimal(splits[0])

        self.feature = None

        if len(splits) > 1:
            self.feature = splits[1]
            remaining = input[len(self.feature) + input.index(self.feature):]
            subs = splitsubs(remaining)

            self.first = DTree(subs[0])
            self.second = DTree(subs[1])

    def __str__(self):
        if self.feature:
            return "Value={0} Feature={1} ({2}) ({3})".format(self.value, self.feature, str(self.first), str(self.second))
        return "Value={0}".format(self.value)

    def apply(self, features):
        curr = Decimal('1.0')
        return self.apply_acc(curr, features)

    def apply_acc(self, curr, features):
        curr *= self.value
        if not self.feature:
            return curr

        if self.feature in features:
            return self.first.apply_acc(curr, features)

        return self.second.apply_acc(curr, features)



def main():

    if len(sys.argv) < 2:
        print "usage: {0} <input-file>".format(__file__)
        sys.exit(-1)

    with open(sys.argv[1]) as _file:
        file = FileReader(_file)

        T = file.int()
        for t in xrange(T):

            L = file.int()

            dtree_input = ' '.join(file.nstring(L))
            root = DTree(dtree_input)

            results = []

            A = file.int()
            for a in xrange(A):

                features = file.strings()[2:]
                results.append(root.apply(features))

            print "Case #{0}:".format(t+1)
            print '\n'.join("%.7f" % (value, ) for value in results)


if __name__ == "__main__":
    main()

