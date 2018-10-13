import string

def check_winner(plays):
    if all([p in ['X', 'T'] for p in plays]):
        return 'X won'
    if all([p in ['O', 'T'] for p in plays]):
        return 'O won'
    else:
        return None

def get_all_combos():
    return [(0,1,2,3),
            (4,5,6,7),
            (8,9,10,11),
            (12,13,14,15),
            (0,4,8,12),
            (1,5,9,13),
            (2,6,10,14),
            (3,7,11,15),
            (0,5,10,15),
            (3,6,9,12)]


def check_done(s):
    if '.' in s:
        return 'Game has not completed'
    else:
        return 'Draw'

def main():

    infile = open('a.in','r')
    outfile = open('a.out','w')

    T = int(string.strip(infile.readline()))    

    for k in xrange(T):
        print k
        s = string.strip(infile.readline())
        s += string.strip(infile.readline())
        s += string.strip(infile.readline())
        s += string.strip(infile.readline())
        infile.readline()
        for (a,b,c,d) in get_all_combos():
            answer = check_winner([s[a], s[b], s[c], s[d]])
            if answer is not None:
                break
        if answer is None:
            answer = check_done(s)

        outfile.write('Case #%d: %s\n' % (k+1,answer))


if __name__ == '__main__':
    main()

