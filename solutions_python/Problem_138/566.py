def war(naomi, ken, size):
    lose = 0
    n = 0
    copy = list(ken)
    while n<size:
        k=0
        while k<size-lose:
            if naomi[n]<copy[k]:
                lose+=1
                copy.remove(copy[k])
                break
            elif naomi[n]>copy[k]:
                k+=1
            else:
                print 'WAR Imposibru', n, k, copy
        n+=1
    return lose

def deceitful_war(filename):
    fin = open(filename, 'r')
    out = open('deceitful_war.out', 'w')
    cases = int(fin.readline())
    case = 1
    while case <= cases:
        size = int(fin.readline())
        naomi = sorted(map(lambda x: float(x), fin.readline().split(' ')))
        ken = sorted(map(lambda x: float(x), fin.readline().split(' ')))
        

        copy = list(ken)

        for n in naomi:
            for k in copy:
                if n > k:
                    copy.remove(k)
                    break

        deceit_wins = size-len(copy) 
        war_wins = size-war(naomi, ken,size)
        out.write('Case #%d: %d %d\n' % (case, deceit_wins, war_wins))
        case+=1

    fin.close()
    out.close()

deceitful_war('D-large.in')