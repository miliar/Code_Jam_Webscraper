import re

def rotated(original):
    return list(map(lambda x: "".join(x), zip(*original)))

def replace(s):
    s = re.sub(r'^([?]+([^?]))', lambda m: m.group(2) * len(m.group(1)), s)
    s = re.sub(r'(([^?])[?]+)', lambda m: m.group(2) * len(m.group(1)), s)
    return s

def solve(cake):
    cake = list(map(replace, cake))
    cake = rotated(cake)
    cake = list(map(replace, cake))
    cake = rotated(cake)
    return "\n".join(cake)

def main():
    t = int(input())
    for i in range(t):
        r, c = map(int, input().split())
        cake = []
        for y in range(r):
            cake.append(input())
        result = solve(cake)
        print("Case #{}:\n{}".format(i + 1, result))

if __name__ == '__main__':
    main()
