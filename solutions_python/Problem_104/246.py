__author__ = 'JJ'
import copy, itertools

# set positive distinct ints S

# two nonempty distinct subsets with same sum

dirt = r'C:\Users\JJ\Downloads\C-small-attempt0 (1).in'
#dirt = r'C:\GCJ\in.txt'

def get_text(filepath):
    with open(filepath, 'r') as inputfile:
        text = inputfile.read()

    text = text.strip().split('\n')

    return text

text = get_text(dirt)

text.pop(0)
outputlist = []
for line in text:
    line = map(int, [x for x in line.strip().split(' ') \
                        if x])[1:]

    holddict = {}
    out = []

    # try against single numbers
    try:
        for x in range(1, len(line)-1):
            for xx in itertools.combinations(line, x):
                thesum = sum(xx)
                if thesum in holddict.keys():
                    out.append(' '.join(map(str,xx)))
                    out.append(holddict[thesum])
                    raise IOError
                else:
                    holddict[thesum] = ' '.join(map(str, xx))
    except IOError:
        outputlist.append('\n'.join(out))
        continue

    outputlist.append("Impossible")

with open(r'C:\GCJ\out.txt', 'w') as outputfile:
    outputfile.write('\n'.join(
        ["Case #%s:\n%s" % (index+1, content) \
        for index, content in enumerate(outputlist)]
    ))


