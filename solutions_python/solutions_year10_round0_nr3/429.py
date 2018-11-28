from collections import deque

def oneday(l, R, k):
    cash = 0
    # for each run:
    for i in range(R):
        # load up, adding to cash
        c = 0
        for i in range(len(l)):
            if c + l[0] > k: break
            c += l[0]
            l.rotate(-1)
        cash += c
    return cash

if __name__ == "__main__":
    fname = "C-small-attempt0.in"
    lines = open(fname).readlines()
    T = int(lines.pop(0))
    for i in range(T):
        R, k, N = map(int, lines.pop(0).split())
        l = map(int, lines.pop(0).split())
        cash = oneday(deque(l), R, k)
        print "Case #" + str(i + 1) + ":",cash
