import sys


def solve(pancakes):
    minutes = 0
    # First phase is distribution. Distribution should only happen if you take
    # the max, divide it by 2 and take all plates with more pancakes than that
    # number and distribute those into other plates. Then take which one is
    # a better choice: split or keep.
    while True:
        pancakes = sorted(pancakes)
        max_pancake = max(pancakes)
        counter = 0
        should_split = False
        result = pancakes
        for i in range(0, len(pancakes)):
            result = sorted(result)
            last = result[-1]
            # Bug is that 9 can be evenly split into 3 3 3
            if last == 9 and (len(result) == 1 or max(result[:-1]) < 5
                              or result.count(6) == 1):
                result = result[:-1] + [6, 3]
            else:
                result = result[:-1] + [last / 2, last - last / 2]
            counter += 1
            if max(result) + counter <= max_pancake:
                pancakes = result
                minutes += counter
                should_split = True
                break
        if not should_split:
            break

    minutes += max(pancakes)
    return minutes


def test():
    assert solve([6, 2]) == 4
    assert solve([1, 1, 1, 1, 4]) == 3
    assert solve([1, 1, 4, 3, 3]) == 4
    assert solve([1, 1, 5, 5, 9, 9]) == 7
    assert solve([1, 2, 1, 2]) == 2
    assert solve([1, 3, 4]) == 4
    assert solve([1, 3, 7, 9]) == 7
    assert solve([1, 3]) == 3
    assert solve([1, 4, 1, 8, 5]) == 6
    assert solve([1, 4, 4, 5, 1]) == 5
    assert solve([1, 4, 7]) == 5
    assert solve([1, 5, 5]) == 5
    assert solve([1, 7, 9, 8]) == 8
    assert solve([1, 8, 3, 1]) == 5
    assert solve([1, 8, 8]) == 6
    assert solve([1, 9, 2, 5]) == 6
    assert solve([1, 9, 3]) == 5
    assert solve([1, 9, 8, 6]) == 8
    assert solve([1]) == 1
    assert solve([2, 1]) == 2
    assert solve([2, 2, 1, 3, 3]) == 3
    assert solve([2, 2, 3, 5, 5]) == 5
    assert solve([2, 2, 4, 5, 4]) == 5
    assert solve([2, 2, 7]) == 5
    assert solve([2, 3, 1, 5, 3]) == 4
    assert solve([2, 4, 8]) == 5
    assert solve([2, 5, 5]) == 5
    assert solve([2, 5, 7, 2]) == 6
    assert solve([2, 5]) == 4
    assert solve([2, 6, 2, 1]) == 4
    assert solve([2, 6, 6, 6]) == 6
    assert solve([2, 9, 6]) == 6
    assert solve([2, 9, 8, 9]) == 8
    assert solve([2, 9, 9, 9, 3, 3]) == 8
    assert solve([2]) == 2
    assert solve([3, 1, 2, 5, 4]) == 5
    assert solve([3, 1, 3, 2, 5]) == 4
    assert solve([3, 1, 9]) == 5
    assert solve([3, 2, 1]) == 3
    assert solve([3, 2, 8, 3, 7]) == 6
    assert solve([3, 2, 9, 5]) == 6
    assert solve([3, 3, 4]) == 4
    assert solve([3, 3, 5, 5, 9, 9]) == 7
    assert solve([3, 3, 7]) == 5
    assert solve([3, 4, 4, 6]) == 5
    assert solve([3, 6, 6, 6, 9, 9]) == 8
    assert solve([3, 7, 9]) == 7
    assert solve([3, 8, 3]) == 5
    assert solve([3]) == 3
    assert solve([4, 1, 4]) == 4
    assert solve([4, 2, 5]) == 5
    assert solve([4, 2, 8]) == 5
    assert solve([4, 3, 2, 1]) == 4
    assert solve([4, 3, 4]) == 4
    assert solve([4, 4, 5, 4, 3]) == 5
    assert solve([4, 6, 1, 5]) == 6
    assert solve([4, 7, 4]) == 5
    assert solve([4, 8, 6, 6]) == 7
    assert solve([4, 8]) == 5
    assert solve([4, 9]) == 6
    assert solve([4]) == 3
    assert solve([5, 1, 1, 5, 1]) == 5
    assert solve([5, 1, 3, 1, 2]) == 4
    assert solve([5, 2, 1, 2, 3]) == 4
    assert solve([5, 2, 1, 4, 1]) == 5
    assert solve([5, 2, 8]) == 6
    assert solve([5, 3, 2, 1, 4]) == 5
    assert solve([5, 3, 4, 3, 5]) == 5
    assert solve([5, 3, 4, 5]) == 5
    assert solve([5, 3, 5, 2, 1]) == 5
    assert solve([5, 3, 5]) == 5
    assert solve([5, 4, 1, 3, 1]) == 5
    assert solve([5, 4, 2, 2, 5]) == 5
    assert solve([5, 4, 3, 2, 1]) == 5
    assert solve([5, 4, 5, 6]) == 6
    assert solve([5, 4, 5]) == 5
    assert solve([5, 5, 5, 5, 9, 9]) == 7
    assert solve([5, 5, 5, 9, 9, 9]) == 8
    assert solve([5, 5]) == 5
    assert solve([5, 6, 9, 6, 9, 6]) == 8
    assert solve([5, 7, 9]) == 7
    assert solve([5, 8, 2]) == 6
    assert solve([5, 9, 7, 7]) == 8
    assert solve([5, 9, 7]) == 7
    assert solve([5]) == 4
    assert solve([6, 1, 8, 8, 2]) == 7
    assert solve([6, 3, 8]) == 6
    assert solve([6, 3, 9]) == 6
    assert solve([6, 5, 4, 3, 2, 1]) == 6
    assert solve([6, 5, 4]) == 6
    assert solve([6, 5, 7]) == 7
    assert solve([6, 6, 5, 6]) == 6
    assert solve([6, 6, 6, 6, 9, 9]) == 8
    assert solve([6, 6, 9, 3]) == 7
    assert solve([6, 6, 9, 4]) == 7
    assert solve([6, 6]) == 5
    assert solve([6, 7, 3]) == 6
    assert solve([6]) == 4
    assert solve([7, 1, 4, 2]) == 5
    assert solve([7, 4, 8, 5, 3]) == 7
    assert solve([7, 5, 2]) == 6
    assert solve([7, 5, 3]) == 6
    assert solve([7, 6, 3]) == 6
    assert solve([7, 6, 4]) == 6
    assert solve([7, 7, 7, 7, 7, 9]) == 8
    assert solve([7, 7]) == 6
    assert solve([7, 8, 8, 2]) == 7
    assert solve([7, 9, 2, 7, 9]) == 9
    assert solve([7]) == 5
    assert solve([8, 1, 3, 4]) == 5
    assert solve([8, 1, 6, 2]) == 6
    assert solve([8, 1, 8]) == 6
    assert solve([8, 3, 1]) == 5
    assert solve([8, 4]) == 5
    assert solve([8, 5, 2]) == 6
    assert solve([8, 5, 4]) == 6
    assert solve([8, 6, 1, 1]) == 6
    assert solve([8, 6, 3, 1]) == 6
    assert solve([8, 8, 3]) == 6
    assert solve([8, 8, 8, 8, 8]) == 8
    assert solve([8, 8, 8, 8]) == 8
    assert solve([8, 8, 8]) == 7
    assert solve([8, 8]) == 6
    assert solve([8, 9, 1, 1]) == 7
    assert solve([8, 9, 3]) == 7
    assert solve([8]) == 5
    assert solve([9, 2, 1, 4]) == 6
    assert solve([9, 4, 5, 8]) == 7
    assert solve([9, 4, 6, 5]) == 7
    assert solve([9, 5, 1]) == 6
    assert solve([9, 5, 3, 5]) == 6
    assert solve([9, 5, 4, 8]) == 7
    assert solve([9, 5, 8, 2, 9]) == 8
    assert solve([9, 6, 2, 6]) == 7
    assert solve([9, 6]) == 6
    assert solve([9, 7, 3, 2]) == 7
    assert solve([9, 7]) == 7
    assert solve([9, 8]) == 7
    assert solve([9, 9, 3, 4]) == 7
    assert solve([9, 9, 9, 9, 9, 9]) == 9
    assert solve([9, 9, 9, 9, 9]) == 9
    assert solve([9, 9, 9, 9]) == 9
    assert solve([9, 9, 9]) == 8
    assert solve([9, 9]) == 7
    assert solve([9]) == 5


def main():
    output = []
    with open('input.in') as f:
        lines = f.readlines()
        for i in range(2, len(lines), 2):
            pancakes = [int(x) for x in lines[i].rstrip().split(' ')]
            # print pancakes, solve(pancakes)
            output.append(solve(pancakes))

    with open('output.out', 'w') as of:
        content = ['Case #{i}: {ans}'.format(i=(i+1), ans=out)
                   for i, out in enumerate(output)]
        of.write('\n'.join(content))


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test()
    else:
        main()
