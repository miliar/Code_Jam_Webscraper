def solve():
    line = input()
    n, line = line.split(' ')
    n = int(n)
    num_with_shyness = [int(digit) for digit in list(line)]
    num_have = 0
    num_extra = 0
    assert num_with_shyness[n] != 0
    for num_required in range(n+1):
        while num_have < num_required:
            num_have += 1
            num_extra += 1
        num_have += num_with_shyness[num_required]
    print(num_extra)

if __name__ == '__main__':
    cases = int(input())
    for case in range(1, cases+1):
        print('Case #%d: ' % (case,), end='')
        solve()
