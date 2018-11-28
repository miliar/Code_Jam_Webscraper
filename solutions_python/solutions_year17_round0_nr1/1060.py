from collections import deque

def solve():
    ls, k = input().rstrip().split()
    ls = list(ls)
    k = int(k)
    count = 0
    i = 0
    while i < len(ls):
        if ls[i] == '-':
            if i + k > len(ls):
                return 'IMPOSSIBLE'
            for j in range(i, i + k):
                ls[j] = '+' if ls[j] == '-' else '-'
            count += 1
        i += 1
    if '-' in ls:
        return 'IMPOSSIBLE'
    else:
        return count


if __name__ == '__main__':
    t = int(input().rstrip())
    for i in range(1, t + 1):
        print('CASE #' + str(i) + ': ' + str(solve()))
