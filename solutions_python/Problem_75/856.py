"""
Daniel Herde
usage: solution.py file.in > file.out
"""

import sys

path = sys.argv[1]

def parse(line):
    data = (line.rstrip()).split(' ')
    filters = {}
    for i in range(int(data.pop(0))):
        triple = data.pop(0)
        filters[triple[0]+triple[1]]=triple[2]
        filters[triple[1]+triple[0]]=triple[2]

    opposed = []
    for i in range(int(data.pop(0))):
        opp = data.pop(0)
        opposed.append([opp[0], opp[1]])

    data.pop(0)
    return filters, opposed, data[0]

import pdb

def evaluate(filters, opposed, data):
    final = []
    count = {}

    for initchar in map(chr, range(65, 91)):
        count[initchar]=0

    for char in data:
        final.append(char)
        count[char]+=1

        # apply the filters
        try:
            newchar = filters["".join(final[-2:])]
            count[final[-1]]-=1
            count[final[-2]]-=1

            final = final[:-2]
            final.append(newchar)
            count[newchar]+=1
        except:
            pass

        # check for the eliminations
        for opp in opposed:
            if count[opp[0]]>0 and count[opp[1]]>0:
                final = []
                for celim in count:
                    count[celim]=0

    return final

def run(path):
    f = open(path,'r')
    lines = f.readlines()[1:]
    f.close()

    for i, line in enumerate(lines):
        result = evaluate(*parse(line))
        print "Case #"+str(i+1)+': ['+', '.join(result)+']'

run(path)
