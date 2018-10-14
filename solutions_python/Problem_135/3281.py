import fileinput

def main():
    bad = 'Bad magician!'
    cheat = 'Volunteer cheated!'
    num_cases = int(raw_input())
    for i in xrange(num_cases):
        a1 = int(raw_input())
        for j in xrange(4):
            num = map(int, raw_input().split(' '))
            if a1 == j + 1:
                s1 = set(num)

        a2 = int(raw_input())
        for j in xrange(4):
            num = map(int, raw_input().split(' '))
            if a2 == j + 1:
                s2 = set(num)

        print 'Case #%s: ' % (i+1),
        inter = s1 & s2
        if len(inter) == 0:
            print cheat
            continue
        if len(inter) == 1:
            for k in inter:
                print k
            continue
        print bad
        

if __name__ == '__main__':
    main()
