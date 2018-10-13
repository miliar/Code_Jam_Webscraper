from __future__ import division

from sys import stdin, stdout
from basics import *

def solve(D, N, horses):
    longest = max((D - k) / s for k, s in horses)
    return D / longest

T = int(stdin.readline())

for t in range(T):
    D, N = read_vals()
    horses = read_lines(N)

    result = solve(D, N, horses)

    stdout.write("Case #{}: {}\n".format(t+1, result))