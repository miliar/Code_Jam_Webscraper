import sys


def solve(num):
    num = list(str(num))
    changed = True
    while changed:
        changed = False
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                num[i] = chr(ord(num[i]) - 1)
                for j in range(i + 1, len(num)):
                    num[j] = '9'
                changed = True
    return int(''.join(num))

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()
    T = int(lines.pop(0))

    result = ''
    for i in range(T):
        result += 'Case #{idx}: {result}\n'.format(idx=i+1, result=solve(lines.pop(0)))

    print(result)
    with open('output.txt', 'w') as f:
        f.write(result)
