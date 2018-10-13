#!/usr/bin/python

in_file = "tongues.in"
out_file = "tongues.out"

def get_letter(let):
    if let == 'a':
        return 'y'
    elif let == 'b':
        return 'h'
    elif let == 'c':
        return 'e'
    elif let == 'd':
        return 's'
    elif let == 'e':
        return 'o'
    elif let == 'f':
        return 'c'
    elif let == 'g':
        return 'v'
    elif let == 'h':
        return 'x'
    elif let == 'i':
        return 'd'
    elif let == 'j':
        return 'u'
    elif let == 'k':
        return 'i'
    elif let == 'l':
        return 'g'
    elif let == 'm':
        return 'l'
    elif let == 'n':
        return 'b'
    elif let == 'o':
        return 'k'
    elif let == 'p':
        return 'r'
    elif let == 'q':
        return 'z'
    elif let == 'r':
        return 't'
    elif let == 's':
        return 'n'
    elif let == 't':
        return 'w'
    elif let == 'u':
        return 'j'
    elif let == 'v':
        return 'p'
    elif let == 'w':
        return 'f'
    elif let == 'x':
        return 'm'
    elif let == 'y':
        return 'a'
    elif let == 'z':
        return 'q'
    return let

def main():
    f = open(in_file, 'r')
    g = open(out_file, 'w')
    cases = int(f.readline())
    case = 0
    while True:
        case += 1
        tgt = f.readline()
        if tgt == '':
            break
        g.write('Case #%d: ' % case)
        for c in tgt:
            map_c = get_letter(c)

            g.write(map_c)
    g.write("\n")
    print 'done'

if __name__ == "__main__":
    main()
