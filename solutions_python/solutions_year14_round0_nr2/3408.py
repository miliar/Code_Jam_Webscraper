
import sys

def get_input():
    return sys.stdin.read().splitlines()

def split_input(str, separator = ' ', func = None):
    list = str.split(separator)
    if not func is None:
        list = map(func, list)
    return list

def calc_time(n, C, F, X):
    x = X / (2 + n * F)
    for i in range(0, n):
        x += C / (2 + i * F)
    return x

def try_case(str):
    C, F, X = split_input(str, func=float)
    min = calc_time(0, C, F, X)
    n = 0
    while True:
        n += 1
        t = calc_time(n, C, F, X)
        if t < min:
            min = t
        else:
            break
    return min

def output(x, y):
    print("Case #{0}: {1:.7f}".format(x, y))

def main():
    lines = get_input()
    T = int(lines.pop(0))
    
    for n in range(1, T + 1):
        ret = try_case(lines.pop(0))
        output(n, ret)
    

if __name__ == '__main__':
    main()
