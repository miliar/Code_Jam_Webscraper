__author__ = 'j0hnny'


if __name__ == '__main__':
    results = []

    with open('A-small-attempt2.in', 'r') as input:
        cases = int(input.readline())
        for case in range(cases):
            (P, Q) = input.readline().split('/')
            P = int(P)
            Q = int(Q)
            print P, Q

            div = 3
            while div <= P:
                if P % div == 0 and Q % div == 0:
                    P /= div
                    Q /= div
                div += 1

            g = 0
            while Q > 1:
                if Q % 2 != 0:
                    g = None
                    break
                else:
                    if P < Q:
                        g += 1
                    Q /= 2

            if g is None:
                results.append('impossible')
            else:
                results.append(g)

    with open('output', 'w') as output:
        for case in range(cases):
            res = results[case]
            s = 'Case #%d: %s\n' % (case+1, res)
            print s
            output.write(s)