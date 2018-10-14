def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        fst = int(raw_input()) - 1
        for i in xrange(4):
            if i == fst:
                s1 = set(map(int, raw_input().split()))
            else:
                raw_input()
        snd = int(raw_input()) - 1
        for i in xrange(4):
            if i == snd:
                s2 = set(map(int, raw_input().split()))
            else:
                raw_input()
        mul = s1 & s2
        if len(mul) == 0:
            print 'Case #{0}: Volunteer cheated!'.format(t)
        elif len(mul) == 1:
            print 'Case #{0}: {1}'.format(t, mul.pop())
        else:
            print 'Case #{0}: Bad magician!'.format(t)
if __name__ == '__main__':
    main()
