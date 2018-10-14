import sys
from pprint import pprint

phrase = 'welcome to code jam'

def main():
    N = int(sys.stdin.readline().strip())
    for i in xrange(N):
        text = sys.stdin.readline().strip()
        front = {0: 1}
        sum = 0
        for j in xrange(len(text)):
            add = {}
            remove = set([])
            # prune
            for key in front:
                if len(phrase) - key > len(text) - j:
                    remove.add( key )
                if key == len(phrase):
                    sum = (sum + front[key]) % 10000
                    remove.add( key )
            for key in remove:
                del front[key]
            # extend
            for f in front:
                if phrase[f] == text[j]:
                    if f+1 in add:
                        sofar = add[f+1]
                        add[f+1] = sofar + front[f]
                    else:
                        add[f+1] = front[f]
            for key in add:
                if key in front:
                    front[key] = front[key] + add[key]
                else:
                    front[key] = add[key]
        for key in front:
            if key == len(phrase):
                sum = (sum + front[key]) % 10000
        print 'Case #%d: %04d' % (i+1, sum)


if __name__ == "__main__":
    main()
