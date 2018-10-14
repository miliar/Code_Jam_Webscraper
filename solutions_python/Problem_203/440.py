import numpy as np


def arrange(initials):
    for i in range(len(initials)):
        prev_val = '?'
        for j in range(len(initials[0])):
            if (initials[i])[j] != '?':
                prev_val = (initials[i])[j]
            else:
                (initials[i])[j] = prev_val
    # print(initials)
    return initials


def reverse(hlist):
    rev = []
    for l in hlist:
        rev.append(l[::-1])
    return rev


def run():
    inp = input()
    R, C = (int(i) for i in inp.split(' '))
    hlist = []
    for index in range(R):
        hlist.append(list(input()))

    hlist = arrange(hlist)
    hlist = reverse(arrange(reverse(hlist)))

    hlist = np.array(hlist)

    hlist = arrange(hlist.T)
    hlist = reverse(arrange(reverse(hlist)))
    hlist = np.array(hlist).T

    for x in hlist:
        print(''.join(x))


if __name__ == '__main__':
    for case in range(int(input())):
        print("Case #%d: " % (case + 1))
        run()
