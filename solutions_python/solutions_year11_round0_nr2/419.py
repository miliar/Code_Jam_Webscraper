#!/usr/bin/env python3

class elem(object):
    def __init__(self, symb):
        self.symb = str(symb)
        self.comb = list()
        self.opposed = list()
    def __repr__(self):
        return self.symb

data = open('wiz.in')

for i in range(int(data.readline())):
    element_list = list()
    elements = dict()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in range(len(alphabet)):
        element_list.append(elem(alphabet[letter]))
        elements[alphabet[letter]] = element_list[letter]
    line = data.readline().split(' ')
    combs = int(line[0])+1
    combining = line[1:combs]
    for comb_item in combining:
        elements[comb_item[0]].comb.append((comb_item[1], comb_item[2]))
        elements[comb_item[1]].comb.append((comb_item[0], comb_item[2]))
    opps = int(line[combs])+1
    opposing = line[combs+1:combs+opps]
    for opp_item in opposing:
        elements[opp_item[0]].opposed.append(opp_item[1])
        elements[opp_item[1]].opposed.append(opp_item[0])
    invoks = line[-1]
    invoked = []
    for inv in invoks:
        if inv in 'QWERASDF':
            combined = False
            if len(invoked):
                for cb in elements[inv].comb:
                    if cb[0] == repr(invoked[-1]):
                        combined = True
                        del invoked[-1]
                        invoked.append(elements[cb[1]])
                        break
            if not combined:
                invoked.append(elements[inv])
            if len(invoked[:-1]):
                for opp_test in invoked:
                    if repr(opp_test) in invoked[-1].opposed:
                        invoked = list()
                        break
    print('Case #%d: %s' % (i+1, repr(invoked)))

