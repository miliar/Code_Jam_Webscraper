import sys, re

def rstr(in_file=sys.stdin):
    return in_file.readline().strip()

def rint(in_file=sys.stdin):
    return int(rstr(in_file))

MAKERE = re.compile(r'(\w)(\w+\))')

def run():
    wordlen, n_words, n_cases = [int(x) for x in rstr().split()]
    words = []
    for w in range(n_words):
        words.append(rstr())
    for c in range(n_cases):
        case = rstr()
        # Turn into a proper regex
        prev = ''
        while prev != case:
            prev = case
            case = MAKERE.sub(r'\1|\2', case)
        WORD_RE = re.compile(case)
        total = 0
        for m in words:
            if WORD_RE.match(m):
                total +=1
        print 'Case #%s: %s' % (c+1, total)
        
run()