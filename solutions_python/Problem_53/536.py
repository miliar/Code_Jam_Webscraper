import sys
import math

def get_number(base, lang, num):
    if num < base:
        return lang[num]
    else:
        c = num / base
        if c < base:
            return  get_number(base, lang, num % base) + lang[c]
        else:
            return get_number(base, lang, num % base) + get_number(base, lang, c)

def get_state(snappers, times):
    light = "OFF"
    result = get_number(2,"01", times)
    if snappers <= len(result) and result[:snappers] == ("1" * snappers):
        light = "ON"
    return light

fname = "A-large"
debug = False
inp = open(fname + ".in", "r")
out = None
if debug:
    out = sys.stdout
else:
    out = open(fname + ".out", "w")
num_cases = int(inp.readline())
for i in xrange(num_cases):
    out.write("Case #%d: " % (i+1))
    snaps, times = inp.readline().strip().split(' ')
    out.write(get_state(int(snaps), int(times)) + '\n')
