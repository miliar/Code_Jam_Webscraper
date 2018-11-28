from collections import deque
from sys import stdin
lines = deque(line.strip() for line in stdin.readlines())

def nextline():
    return lines.popleft()

def types(cast):
    return tuple(int(x) for x in nextline().split())

def ints():
    return types(int)

def strs():
    return nextline().split()

def main():
    # lines will now contain all of the input's lines in a list
    T = int(nextline())
    for testCase in range(1, T + 1):
        n = list(map(int, nextline()))
        if n != sorted(n):
            i = 1
            while n[i] >= n[i-1]:
                i += 1
            n[i] -= 1
            while i > 0 and (n[i] < 0 or n[i-1] > n[i]):
                i -= 1
                n[i] -= 1
            for j in range(i+1, len(n)):
                n[j] = 9
        if n[0] == 0:
            n = n[1:]
        print("Case #{:d}: {}".format(testCase, ''.join(map(str, n))))

if __name__ == '__main__':
    main()
