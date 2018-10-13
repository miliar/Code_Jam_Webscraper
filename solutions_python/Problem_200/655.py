'''
by aditya76
'''
from io import StringIO
import sys
def main():
    timess = parse_input()
    for i, N in timess:
        r = adi(N)
        print(f'Case #{i}: {r}')
def parse_input():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        yield i, N
def adi(N):
    n = [int(x) for x in str(N)]
    while True:
        for i, (digit, agladigit) in enumerate(zip(n, n[1:])):
            if digit > agladigit:
                break
        else:
            return int(''.join(str(x) for x in n))
        n[i] -= 1
        for j in range(i+1, len(n)):
            n[j] = 9
if __name__ == '__main__':
    main()
