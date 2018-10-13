
import sys

def get_input():
    return sys.stdin.read().splitlines()

def split_input(str, separator = ',', func = None):
    list = str.split(separator)
    if not func is None:
        list = map(func, list)
    return list

def parse_grid(lines):
    
    pass

def try_case(lines):
    num1 = split_input(lines[int(lines[0])], ' ', func=int)
    lines = lines[5:]
    num2 = split_input(lines[int(lines[0])], ' ', func=int)
    lines = lines[5:]
    return set(num1) & set(num2)

def output(x, y):
    print("Case #{0}: {1}".format(x, y))

def main():
    lines = get_input()
    T = int(lines.pop(0))
    
    for n in range(1, T + 1):
        ret = try_case(lines[:10])
        if len(ret) == 1:
            output(n, ret.pop())
        elif len(ret) > 0:
            output(n, "Bad magician!")
        elif len(ret) == 0:
            output(n, "Volunteer cheated!")
        lines = lines[10:]
    

if __name__ == '__main__':
    main()
