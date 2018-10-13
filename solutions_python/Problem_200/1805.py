import sys
import collections

def find_decreasing(digits):
    for i in range(len(digits) - 1):
        if digits[i+1] < digits[i]:
            return i
    return None

def solve(N):
    digits = [ch for ch in N]
    idx = find_decreasing(digits)
    while idx is not None:
        if digits[idx] == '1':
            return '9' * (len(digits) - 1)
        digits[idx+1:] = '9' * (len(digits) - idx - 1)
        digits[idx] = chr(ord(digits[idx]) - 1)
        idx = find_decreasing(digits)
    return ''.join(digits)

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        T = int(f.readline().strip())
        for case in range(T):
            N = f.readline().strip()
            print('Case #{}: {}'.format(case + 1, solve(N)))
