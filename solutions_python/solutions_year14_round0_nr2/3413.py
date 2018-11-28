import sys
sys.setrecursionlimit(10000000)


__author__ = 'iraasta'



def start():
    t = range(int(raw_input()))
    for a in t:
        run(a+1)


def run(case):
    _input = raw_input().split(" ")
    c = float(_input[0])
    f = float(_input[1])
    x = float(_input[2])
    gameCycle(0.0, 2.0, c, f, x, None, case)


def gameCycle(time, actual,c,f,x,lastwintime, case):
    farmtime = c/actual
    wintime = x/actual

    if farmtime > time+wintime:
        print "Case #{0}: {1:.7f}".format(case, time+wintime)
        return
    if not lastwintime is None and lastwintime < time+wintime:
        print "Case #{0}: {1:.7f}".format(case, lastwintime)
        return
    gameCycle(time+farmtime, actual + f, c, f, x, time + wintime, case)

if __name__ == "__main__":
    start()