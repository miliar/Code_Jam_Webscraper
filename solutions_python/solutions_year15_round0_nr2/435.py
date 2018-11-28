__author__ = 'ctynan'


def main():
    f_in = open('/Users/ctynan/Downloads/B-large.in', 'r')
    f_out = open('/Users/ctynan/Downloads/B-large.out', 'w')

    T = int(f_in.readline())

    cost = {}

    for i in range(1001):
        if i == 0:
            continue

        for j in range(1001):
            cost[(j, i)] = int((j-1) / i)


    for tst in range(T):
        D = int(f_in.readline().strip('\n'))
        P = f_in.readline().strip('\n').split(' ')
        P = map(lambda x: int(x), P)

        best = 10000

        for i in range(1001):
            if i == 0:
                continue
            minutes = i
            for j, v in enumerate(P):

                minutes += cost[(v, i)]

            best = min(best, minutes)

        f_out.write(("Case #%i: %i\n") % (tst+1, best))

    return

def __init__():
    pass

main()


