def build_index(s):
    ref = 'welcome to code jam'
    d = {}
    for i in ref:
        d[i] = []
    for i in range(len(s)):
        if s[i] in ref:
            d[s[i]].append(i)

    return d

def welcome_count(s):
    ref = 'welcome to code jam'
    d = build_index(s)
    n = 0

    for j0 in d['w']:
        for j1 in d['e']:
            if j1 > j0:
                for j2 in d['l']:
                    if j2 > j1:
                        for j3 in d['c']:
                            if j3 > j2:
                                for j4 in d['o']:
                                    if j4 > j3:
                                        for j5 in d['m']:
                                            if j5 > j4:
                                                for j6 in d['e']:
                                                    if j6 > j5:
                                                        for j7 in d[' ']:
                                                            if j7 > j6:
                                                                for j8 in d['t']:
                                                                    if j8 > j7:
                                                                        for j9 in d['o']:
                                                                            if j9 > j8:
                                                                                for j10 in d[' ']:
                                                                                    if j10 > j9:
                                                                                        for j11 in d['c']:
                                                                                            if j11 > j10:
                                                                                                for j12 in d['o']:
                                                                                                    if j12 > j11:
                                                                                                        for j13 in d['d']:
                                                                                                            if j13 > j12:
                                                                                                                for j14 in d['e']:
                                                                                                                    if j14 > j13:
                                                                                                                        for j15 in d[' ']:
                                                                                                                            if j15 > j14:
                                                                                                                                for j16 in d['j']:
                                                                                                                                    if j16 > j15:
                                                                                                                                        for j17 in d['a']:
                                                                                                                                            if j17 > j16:
                                                                                                                                                for j18 in d['m']:
                                                                                                                                                    if j18 > j17:
                                                                                                                                                        n = n + 1


    tmp = ('0000' + str(n)[-4:])[-4:]
    return tmp
