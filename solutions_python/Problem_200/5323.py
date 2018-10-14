def check(n):
    last = len(n) - 1
    while last > 0:
        if not int(n[last]) >= int(n[last - 1]):
            return False
        last -= 1
    return True

def solve(N):
    while N > 9:
        if check(str(N)):
            return N
        N -= 1
    return N

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        print('Case #{}: {}'.format(t + 1, solve(N)))

if __name__ == '__main__':
    main()
