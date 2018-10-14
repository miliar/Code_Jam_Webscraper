import sys

def main(argv):
    map = {'a': 'y','b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q'}
    file = open(argv[1])
    case = 0
    for line in file:
        if (case == 0):
            case = 1
            continue
        str = 'Case #%d: ' % case
        case += 1
        for i in line:
            if (i == '\n'): continue
            str += map.get(i, i)
        print str
     
if __name__ == "__main__":
    main(sys.argv)