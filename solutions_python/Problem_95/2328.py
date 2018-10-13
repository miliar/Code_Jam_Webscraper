input_file = 'tests.txt'

mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h',
           'e': 'o', 'd': 's', 'g': 'v', 'f': 'c',
           'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u',
           'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b',
           'p': 'r', 's': 'n', 'r': 't', 'u': 'j',
           't': 'w', 'w': 'f', 'v': 'p', 'y': 'a',
           'x': 'm', 'q': 'z', 'z': 'q'}

def solve(line):
    return ''.join(mapping[x] for x in line)

def main():
    fh = open(input_file)
    test_cases = int(fh.readline())
    for case in xrange(test_cases):
        print 'Case #%s: %s' % (case + 1, solve(fh.readline()[:-1]))
    
    
if __name__ == '__main__':
    main()
