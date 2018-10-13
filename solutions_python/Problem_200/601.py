# coding: utf8
# Copyright: MathDecision


def last_number(x):
    i = 0
    while i + 1 < len(x):
        if x[i] > x[i + 1]:
            x[i] -= 1
            for j in range(i + 1, len(x)):
                x[j] = 9
            return x
        elif x[i] == x[i + 1]:
            j = i + 1
            fl = False
            while j + 1 < len(x):
                if x[j] < x[j + 1]:
                    i = j + 1
                    fl = True
                    break
                elif x[j] > x[j + 1]:
                    x[i] -= 1
                    for k in range(i + 1, len(x)):
                        x[k] = 9
                    return x
                else:
                    j += 1
            if fl == False:
                return x
        else:
            i += 1
    return x


def str2list(x):
    return [int(xx) for xx in x if xx != '\n']

def list2str(x):
    strconv = ''.join([str(xx) for xx in x])
    if strconv[0] == '0' and len(strconv) > 1:
        return strconv[1:]
    else:
        return strconv


if __name__ == '__main__':
    responses = []
    inf = 'tidy2.in'
    outf = 'tidy2.out'
    with open(inf, 'r') as f:
        cases = int(f.readline())
        for i in range(cases):
            numb = f.readline()
            x = str2list(numb)
            res = last_number(x)
            responses.append(list2str(res))
    with open(outf, 'w') as f:
        for i, r in enumerate(responses):
            f.write('Case #{}: {}\n'.format(i + 1, r))

    #
    # x = '20'
    # x = str2list(x)
    # x = last_number(x)
    # print list2str(x)