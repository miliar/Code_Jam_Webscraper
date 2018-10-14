import sys

def rl(*args):
    return sys.stdin.readline().strip()

def main():
    T = int(rl())
    for i in range(1, T+1):
        row1 = int(rl()) - 1
        s1 = set(map(rl, range(4))[row1].split())
        row2 = int(rl()) - 1
        s2 = set(map(rl, range(4))[row2].split())
        p = s1 & s2
        if not p:
            print 'Case #%d: %s' % (i, 'Volunteer cheated!')
        elif len(p) > 1:
            print 'Case #%d: %s' % (i, 'Bad magician!')
        else:
            print 'Case #%d: %s' % (i, p.pop())
            
if __name__ == '__main__':
    main()
