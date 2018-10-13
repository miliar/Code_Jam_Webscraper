import math

def solve(n, k):
    if k == 1:
        mid = (n-1) / 2
        return math.ceil(mid), math.floor(mid)
    if k % 2 == 1:
        return solve(math.floor((n-1) / 2), math.ceil((k-1) / 2))
    else:
        return solve(math.ceil((n-1) / 2), math.ceil((k-1) / 2))

def calculate_lr(stalls, idx):
    lx = 0
    idxl = idx-1
    while idxl >= 0 and stalls[idxl] != 1:
        lx += 1
    rx = 0
    idxr = idx+1
    while idxr < len(stalls) and stalls[idxr] != 1:
        rx += 1
    return lx, rx

def main():
    case_count = int(input())
    for case_no in range(1, case_count+1):
        _n, _k = input().split()
        n = int(_n)
        k = int(_k)
        solution = solve(n, k)
        print('Case #{0}: {1} {2}'.format(case_no, solution[0], solution[1]))

if __name__ == '__main__':
    main()
