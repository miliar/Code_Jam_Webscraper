#!/usr/bin/python -O

import sys
from optparse import OptionParser

def invoke(line):
    info = line.split()
    assert(len(info) >= 4)
    num_combo = int(info[0])
    comb_list = info[1:(1+num_combo)]

    num_opp = int(info[1+num_combo])
    assert(len(info) == (1 + num_combo + 1 + num_opp + 2))
    opp_list = info[(2+num_combo):(len(info)-2)]

    spell = info[len(info) - 1]

    combo_dict = {}
    for combo_str in comb_list:
        combo_dict[''.join(sorted(combo_str[0:2]))] = combo_str[2]

    opp_set = set()
    for opp_str in opp_list:
        opp_set.add(''.join(sorted(opp_str)))

    assert(len(spell) > 0)
    magic = ''
    for spell_char in spell:
        magic += spell_char
        if len(magic) < 2:
            continue

        poss_combo = ''.join(sorted(magic[-2:]))
        if poss_combo in combo_dict:
            magic = magic[:(len(magic)-2)] + combo_dict[poss_combo]
            continue

        for exist_char in magic:
            poss_opp = ''.join(sorted(exist_char + spell_char))
            if poss_opp in opp_set:
                magic = ''
                break;

    return ''.join([x for x in str(list(magic)) if x != "'"])

def main():
    parser = OptionParser("Usage: %prog file ...")
    (options, args) = parser.parse_args()

    fin = open(args[0], 'r')
    lines = fin.readlines()
    lines.pop(0)

    fout = open('output.txt', 'w')

    for i in xrange(len(lines)):
        fout.write("Case #" + str(i+1) + ": " + invoke(lines[i]))
        fout.write('\n')

    fin.close()
    fout.close()
    
if __name__ == '__main__':
    main()
