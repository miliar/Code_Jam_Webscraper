from sys import stdin
def input():
    n = int(stdin.next())
    cases = []
    for i in range(n):
        line = stdin.next()
        N, L, H = [int(x) for x in line.strip().split()]
        line = stdin.next()
        nums = [int(x) for x in line.strip().split()]
        cases.append((L, H, nums))
    return cases

def find(case):
    L, H, nums = case
    for x in range(L, H + 1):
        flag = False
        for num in nums:
            if x % num != 0 and num % x != 0:
                flag = True
                break
        if flag:
            continue
        return x
    return None

def main():
    cases = input()
    for index, case in enumerate(cases):
        result = find(case)
        if not result:
            result = 'NO'
        print 'Case #%d: %s' % (index + 1, result)

main()

