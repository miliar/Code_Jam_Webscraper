import sys

def flip(pancakes, idx, flip_cnt, n):
    return pancakes ^ ((1 << (n - idx)) - (1 << (n - idx - flip_cnt)))


def solve(data):
    pancakes, flip_cnt = data.split()
    flip_cnt = int(flip_cnt)
    n = len(pancakes)
    pancakes = int("".join(str(int(p != "+")) for p in pancakes), 2)

    cur_mask = 1 << (n - 1)
    cnt = 0
    for i in range(n - flip_cnt + 1):
        if pancakes & cur_mask:
            pancakes = flip(pancakes, i, flip_cnt, n)
            cnt += 1
        cur_mask = cur_mask >> 1
    
    if pancakes == 0:
        return cnt
    return "IMPOSSIBLE"


def solve_inputs(inputs):
    cnt = int(inputs[0])
    for i in range(cnt):
        print("Case #{}: {}".format(i + 1, solve(inputs[i+1])))


def main():
    solve_inputs(sys.stdin.readlines())


if __name__ == '__main__':
    main()