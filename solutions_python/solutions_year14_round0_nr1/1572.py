from __future__ import print_function
import sys

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")


T = int(f.readline().strip())

def read_question(fp):
    ans = int(fp.readline().strip())
    cards = [[int(x) for x in fp.readline().strip().split()] for i in range(0, 4)]
    return ans, cards

for case_id in range(1, T+1):
    ans1, cards1 = read_question(f)
    ans2, cards2 = read_question(f)

    line1 = cards1[ans1-1]
    line2 = cards2[ans2-1]

    values = list(set(line1) & set(line2))
    r = 'xxx'
    if len(values) == 0:
        r = 'Volunteer cheated!'
    elif len(values) == 1:
        r = values[0]
    else:
        r = 'Bad magician!'

    print(str.format('Case #{0}: {1}', case_id, r))
