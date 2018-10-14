import re
from string import maketrans

bracket_table = maketrans('()', '[]')
    
def interpret(language, pattern):
    pattern = pattern.translate(bracket_table)
    return [w for w in language if re.match(pattern, w) != None]

def main():
    infile = open('A-large.in', 'r')
    outfile = open('A-large.out', 'w')
    (L,D,N) = map(int, infile.readline().rstrip().split(' '))
    language = [infile.readline().rstrip() for j in xrange(D)]
    for i in xrange(N):
        case = infile.readline().rstrip()
        possible_words = interpret(language, case)
        output = 'Case #%d: %d\n'%(i+1, len(possible_words))
        print output,
        outfile.write(output)
    outfile.close()
    
if __name__ == '__main__':
    main()