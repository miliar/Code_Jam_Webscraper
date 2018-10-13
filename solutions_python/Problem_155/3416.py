__author__ = 'amukherjee14'


def process():

    num_cases = 0
    cases = []
    c = 0
    with open('A-large.in') as f:
        num_cases = int(f.readline().strip())

        for i in xrange(num_cases):
            line = f.readline().split(' ')
            m = int(line[0])
            S = [0]*(m+1)
            for i, v in enumerate(line[1].strip()):
                S[i] = int(v)
            cases.append((S, m))

    f.close()
    target = open('A-large.out', 'w')
    target.truncate()
    for i in xrange(num_cases):
        target.write('Case #'+str(i+1)+': '+ str(mininvite(cases[i][0], cases[i][1])))
        target.write("\n")
    target.close()


def mininvite(S, m):
    if m == 0: return 0
    O = [0]*(m+1)
    O[0] = 0
    O[1] = 1 if S[0] == 0 else 0
    if m == 1: return O[m]
    c = S[0] + S[1]
    for i in xrange(2, m+1):
        d = max(i - c - O[i-1], 0)
        O[i] = O[i-1] + d
        c += S[i]
    return O[m]

if __name__ == '__main__':
    process()