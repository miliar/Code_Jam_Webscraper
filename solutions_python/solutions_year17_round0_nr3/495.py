from collections import defaultdict

def main():
    t = int(input().strip())
    for case in range(1, t + 1):
        n, k = map(int, input().split())
        l = len(bin(k)) - 2
        slices = get_slices(l - 1, n)

        k -= 2**(l-1) - 1
        small = min(slices)
        large = max(slices)
        if k <= slices[large]:
            mini = (large - 1) // 2
            maxi = large // 2
            print('Case #{}: {} {}'.format(case, maxi, mini))
        else:
            mini = (small - 1) // 2
            maxi = small // 2
            print('Case #{}: {} {}'.format(case, maxi, mini))

def get_slices(steps, n):
    slices = defaultdict(lambda: 0)
    slices[n] += 1
    for _ in range(steps):
        newslices = defaultdict(lambda: 0)
        for s in slices:
            if s == 0:
                continue
            if s % 2 == 1:
                newslices[s // 2] += 2 * slices[s]
            else:
                newslices[s // 2] += slices[s]
                newslices[s // 2 - 1] += slices[s]
        slices = newslices
    return slices



if __name__ == '__main__':
    main()
