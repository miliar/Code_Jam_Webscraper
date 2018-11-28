import sys

sys.stdin = open('B-large.in', 'r')
sys.stdout = open('B_large.out', 'w')


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    u = input()
    s = []
    for c in u:
        s.append(c)
    j = 1
    while j < len(s):
        if s[-j] < s[-j - 1]:
            tmp = int(''.join(s))
            tmp2 = int(''.join(s[-j::]))
            tmp -= tmp2 + 1
            s.clear()
            for c in str(tmp):
                s.append(c)
            j = 1
            continue
        else:
            j += 1

    print("Case #{}: {}".format(i, ''.join(s)))
