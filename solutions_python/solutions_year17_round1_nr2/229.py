import math

def compute_windows(requirements, packages):
    """Compute how many servings given packages of ingredients can potentially make."""
    windows = []
    for idx_req, req in enumerate(requirements):
        _win = []
        for amount in packages[idx_req]:
            lower = math.ceil(amount / (req * 1.1))
            upper = math.floor(amount / (req * 0.9))
            if lower <= upper:
                _win.append((lower, upper))
        windows.append(sorted(_win, reverse=True))
    return windows

def check_win_align(windows):
    curr = windows[0]
    for i in range(1, len(windows)):
        if curr[1] < windows[i][0] or windows[i][1] < curr[0]:
            return False
        curr = (max(curr[0], windows[i][0]), min(curr[1], windows[i][1]))
    return True

def solve(requirements, packages):
    all_windows = compute_windows(requirements, packages)
    if any(len(windows) == 0 for windows in all_windows):
        return 0
    indices = [0 for _ in range(len(requirements))]
    kits = 0
    while all(indices[i] < len(all_windows[i]) for i in range(len(requirements))):
        curr_windows = [all_windows[idx][i] for idx, i in enumerate(indices)]
        if check_win_align(curr_windows):
            kits += 1
            for idx, ind in enumerate(indices):
                indices[idx] = ind + 1
        else:
            min_win = min(curr_windows, key=lambda x: x[1])
            for i in range(len(requirements)):
                while indices[i] < len(all_windows[i]) and \
                      all_windows[i][indices[i]][0] > min_win[1]:
                    indices[i] += 1
    return kits

def main():
    case_count = int(input())
    for case_no in range(1, case_count+1):
        input()
        requirements = [int(s) for s in input().split()]
        packages = [[int(s) for s in input().split()] for _ in requirements]
        print('Case #{0}: {1}'.format(case_no, solve(requirements, packages)))

if __name__ == '__main__':
    main()
