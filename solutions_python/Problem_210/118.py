def main(index):
    print 'Case #%d:' % index,
    Ac, Aj = map(int, raw_input().split())
    Acs = sorted([map(int, raw_input().split()) for i in xrange(Ac)])
    Ajs = sorted([map(int, raw_input().split()) for i in xrange(Aj)])

    if Ac == 2:
        if Acs[1][1] - Acs[0][0] <= 720:
            print 2
        elif Acs[0][1] + 1440 - Acs[1][0] <= 720:
            print 2
        else:
            print 4
    elif Aj == 2:
        if Ajs[1][1] - Ajs[0][0] <= 720:
            print 2
        elif Ajs[0][1] + 1440 - Ajs[1][0] <= 720:
            print 2
        else:
            print 4
    else:
        print 2

T = int(raw_input())
for i in xrange(1, T+1):
    main(i)
