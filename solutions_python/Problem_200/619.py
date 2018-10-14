import sys

def solve(num):
    if len(num) == 1:
        return num
    rest = solve(num[1:])
    if rest[0] >= num[0]:
        return num[0] + rest
    return chr(ord(num[0])-1) + ''.join(['9' for _ in rest])

def answer(num):
    return solve(num).lstrip('0')

def main():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        arg = sys.stdin.readline().strip()
        print('Case #{}: {}'.format(i+1, answer(arg)))

if __name__ == '__main__':
    main()
