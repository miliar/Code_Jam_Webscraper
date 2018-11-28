from util import *
from sys import stdin

def f(_):
    n = input()
    xs = sorted(map(int, stdin.readline().split()))
    ys = sorted(map(int, stdin.readline().split()), reverse=True)
    return sum(x*y for (x,y) in zip(xs,ys))

drive(f)
