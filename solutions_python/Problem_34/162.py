import re;
import sys;
import string;

def to_regex(patn):
    tbl = string.maketrans('()','[]');
    return patn.translate(tbl)

def num_matches(patn, words):
    count = 0;
    for w in words:
        if re.match(patn, w):
            count+= 1
    return count

def print_case(num, result):
    print('Case #{0}: {1}'.format(num, result))

case = 1
wordlen, numwords, cases = [int(x) for x in sys.stdin.readline().split()]

words = []
patterns = [];
for x in range(numwords):
    words.append(sys.stdin.readline().rstrip())
for x in range(cases):
    patn = sys.stdin.readline().rstrip()
    patterns.append((case, to_regex(patn)))
    case+=1

results = [(n, num_matches(p, words)) for n,p in patterns]
for r in results:
    print_case(*r)
