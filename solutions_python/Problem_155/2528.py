# -*- coding: utf-8 -*-


def calc(levels):
    cum = 0
    more = 0
    # print levels
    for i, (this, nxt) in enumerate(zip(levels, levels[1:])):
        cum += this
        if i + 1 > cum + more:
            more += i + 1 - (cum + more)
    return more



if __name__ == '__main__':
    f = open("data/A-large.in")
    T = int(f.readline())
    for i in range(0, T):
        line = f.readline().strip()
        sp = line.find(" ")
        max_level = int(line[0:sp])
        levels = [int(x) for x in line[sp+1:max_level+sp+2]]
        solution = calc(levels)
        print "Case #{}: {}".format(i + 1, solution)

