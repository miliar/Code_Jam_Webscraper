# speaking in tongues
#
import sys

def main():

    translations = [
        ('a zoo', 'y qee'),
        ('our language is impossible to understand', 'ejp mysljylc kd kxveddknmc re jsicpdrysi'),
        ('there are twenty six factorial possibilities', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'),
        ('so it is okay if you want to just give up', 'de kr kd eoya kw aej tysr re ujdr lkgc jv')
    ]

    mappings = list(set(sum([zip(*t) for t in translations], [])))
    mappings.append(('q', 'z'))  # the missing link
    mappings = dict(mappings)
    mappings = {v:k for k, v in mappings.items()}
    tests = read_input()
    #import pprint; pprint.PrettyPrinter(indent=4, width=10).pprint(tests); return
    results = map(lambda t: solve(t, mappings), tests)
    print_results(results)


def read_input():
    # read input from stdin
    lines = map(lambda line: line.strip('\n'), sys.stdin.readlines())

    # parse it out
    num_tests = int(lines[0])
    lines = lines[1:]
    tests = lines

    return tests


def print_results(results):
    for i, r in enumerate(results):
        print 'Case #%d: %s' % (i + 1, r)


def solve(test, mappings):
    return ''.join(map(lambda t: mappings[t], test))

main()
