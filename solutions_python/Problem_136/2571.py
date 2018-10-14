# Google Code Jam 2014
# Magic Trick
# Guilherme Rezende <guilhermebr@gmail.com>
# guilhermebr.com

import sys

def calc1(c, x, f, tick, t):
    p = int(x / c)
    #print p
    time = 0
    for a in range(0, p-1):
        time += c / (tick + f*a)
    time1 = time + (c / (tick + f*(p-1))) + (x / (tick + (f * p)))
    time += x / (tick + (f * (p - 1)))
  #  print('Case #%d: %.7f -> %.7f' % (t, time, time1)) 
    print('Case #%d: %.7f' % (t, min(time, time1)))

def calc(c, x, f, tick, t):
    p = int(x / c)
    time = 0
    last_time = time + (x / tick)

    while 1:
        time += c / tick
        tick += f
        timef = time + (x / tick)
        if timef > last_time:
            break
        last_time = timef 

    print('Case #%d: %.7f' % (t, last_time))

def main():
    T = int(raw_input())

    for t in range(1, T+1):
        tick = 2.0
        c, f, x = map(float, raw_input().strip().split())
        calc(c, x, f, tick, t)


if __name__ == '__main__':
    main()