__author__ = 'deniskrut'

# https://code.google.com/codejam/contest/2974486/dashboard#s=p1

import sys
import math

init = 2
proximity = 1
g_section = (math.sqrt(5) + 1) / 2
global cache_max
global cache

def time(i, n, f, x, c):
    global cache_max
    global cache
    #p1 = (2 * i + (n - 1) * f) * n / 2
    #p1 = c / f * math.sqrt(f / i) * math.atan(math.sqrt(n * f / i))
    n_int = int(round(n))
    p1 = 0
    it_start = min(cache_max, n_int)
    if it_start > 0:
        p1 = cache[it_start]
    for it in range(it_start, n_int):
        el = c / (it * f + i)
        p1 += el
        cache[it + 1] = p1
        cache_max = it + 1
    p2 = x / (n_int * f + i)
    return p1 + p2

def minimize_n(n_min, n_max, i, f, x, c, p):
    a = n_min
    b = n_max
    while math.fabs(b - a) >= p:
        n1 = b - ((b - a) / g_section)
        n2 = a + ((b - a) / g_section)
        t1 = time(i, n1, f, x, c)
        t2 = time(i, n2, f, x, c)
        if t1 >= t2:
            a = n1
        else:
            b = n2
    return (a + b) / 2

def optimize_time(n_min, n_max, i, f, x, c):
    best_time = x / i
    time_on_farms = 0
    gain = i
    while True:
        time_on_farms += c / gain
        gain += f
        time_on_build = x / gain
        cur_time = time_on_farms + time_on_build
        if cur_time <= best_time:
            best_time = cur_time
        else:
            break
    return best_time

t_num = int(sys.stdin.readline())

for iteration in range(0, t_num):
    global cache
    global cache_max
    cache = {}
    cache_max = 0

    c, f, x = [float(tmp) for tmp in sys.stdin.readline().split()]
    n_max = int(math.ceil(x / f))
    n_min = 0
    res = optimize_time(n_min, n_max, init, f, x, c)
    #minimized_n = minimize_n(n_min, n_max, init, f, x, c, proximity)
    #normalized_n_min = math.floor(minimized_n)
    #normalized_n_max = math.ceil(minimized_n)
    #t1 = time(init, normalized_n_min, f, x, c)
    #t2 = time(init, normalized_n_max, f, x, c)
    #res = min(t1, t2)
    print "Case #" + str(iteration + 1) + ": " + str(res)
